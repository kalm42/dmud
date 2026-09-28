import { expect, test } from "@playwright/test";
import { parseOperation } from "../src/api/parseOperation.js";
import { expectAccessiblePage } from "./expectAccessiblePage.js";
import { holdDraftCommit } from "./holdDraftCommit.js";

test("SessionZero acknowledges acceptance before any draft commits", async ({
  page,
}) => {
  const barrier = await holdDraftCommit({ page });
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await barrier.reached();
  await expect(page.getByRole("status")).toContainText(
    "no draft has committed yet",
  );
  await expect(page.getByRole("heading", { name: "Session 0" })).toBeFocused();
  await expectAccessiblePage(page);
  await barrier.release();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
});

test("SessionZero recovers the same committed draft on refresh", async ({
  page,
}) => {
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
  const locator = new URL(page.url()).searchParams.get("session0");
  await page.reload();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
  expect(new URL(page.url()).searchParams.get("session0")).toBe(locator);
});

test("SessionZero recovers a lost acceptance response under the original request", async ({
  page,
}) => {
  let original = "";
  await page.route(
    "**/api/session-zero-drafts",
    async (route) => {
      const response = await route.fetch();
      original = parseOperation(await response.json()).operationId;
      await route.abort("failed");
    },
    { times: 1 },
  );
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await expect(page.getByRole("status")).toContainText("Status unavailable");
  const initialLocator = new URL(page.url()).searchParams.get("session0");
  await page.reload();
  expect(new URL(page.url()).searchParams.get("session0")).toBe(initialLocator);
  await expect(page.getByRole("status")).toContainText("outcome unknown");
  await page.getByRole("button", { name: "Recover request" }).click();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
  expect(page.url()).toContain(original);
});

test("SessionZero polls the same subject when SSE is unavailable", async ({
  page,
}) => {
  const barrier = await holdDraftCommit({ page });
  await page.route("**/api/operations/*/events", (route) =>
    route.abort("failed"),
  );
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await barrier.reached();
  await expect(page.getByRole("status")).toContainText(
    "no draft has committed yet",
  );
  await barrier.release();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
});

test("SessionZero preserves retry focus through a failed draft recovery", async ({
  page,
  isMobile,
}) => {
  const barrier = await holdDraftCommit({ page, fail: true });
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await barrier.reached();
  await barrier.release();
  await expect(page.getByRole("status")).toContainText("Failed before commit");
  const retry = page.getByRole("button", { name: "Retry draft" });
  if (!isMobile) {
    await retry.focus();
    await page.keyboard.press("Enter");
  } else {
    await retry.click();
  }
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
  if (!isMobile) await expect(retry).toBeFocused();
  await expect(retry).toHaveAttribute("aria-disabled", "true");
  await expectAccessiblePage(page);
});

test("SessionZero keeps a failed status read distinct from a failed mutation", async ({
  page,
}) => {
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
  await page.route("**/api/operations/*", (route) => route.abort("failed"));
  await page.getByRole("button", { name: "Check status" }).click();
  await expect(page.getByRole("status")).toContainText("Status unavailable");
  await expect(
    page.getByText("Last known state:", { exact: false }),
  ).toContainText("complete");
  await expect(
    page.getByRole("button", { name: "Retry draft" }),
  ).toHaveAttribute("aria-disabled", "true");
});

test("SessionZero retains one logical request under rapid activation", async ({
  page,
}) => {
  const barrier = await holdDraftCommit({ page });
  let submissions = 0;
  page.on("request", (request) => {
    if (
      request.method() === "POST" &&
      request.url().endsWith("/api/session-zero-drafts")
    )
      submissions += 1;
  });
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).dblclick();
  await barrier.reached();
  expect(submissions).toBe(1);
  await barrier.release();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
});

test("SessionZero recovers an interrupted draft using the same subject", async ({
  page,
}) => {
  const barrier = await holdDraftCommit({ page });
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await barrier.reached();
  await expect(page.getByRole("status")).toContainText("Running");
  const initial = page.url();
  await page.getByRole("button", { name: "Cancel start" }).click();
  await expect(page.getByRole("status")).toContainText(
    "Interrupted before commit",
  );
  await barrier.release();
  await page.reload();
  await expect(page.getByRole("status")).toContainText(
    "Interrupted before commit",
  );
  await page.getByRole("button", { name: "Retry draft" }).click();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
  const before = new URL(initial).searchParams.get("session0");
  const after = new URL(page.url()).searchParams.get("session0");
  expect(before?.match(/op_[a-f0-9-]+/)?.[0]).toBe(
    after?.match(/op_[a-f0-9-]+/)?.[0],
  );
});

test("SessionZero recovers a lost retry response without a second attempt", async ({
  page,
}) => {
  const barrier = await holdDraftCommit({ page, fail: true });
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await barrier.reached();
  await barrier.release();
  await expect(page.getByRole("status")).toContainText("Failed before commit");
  await page.route(
    "**/api/operations/*/retry",
    async (route) => {
      await route.fetch();
      await route.abort("failed");
    },
    { times: 1 },
  );
  await page.getByRole("button", { name: "Retry draft" }).click();
  await expect(page.getByRole("status")).toContainText("Status unavailable");
  await page.reload();
  await page.getByRole("button", { name: "Recover request" }).click();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
});
