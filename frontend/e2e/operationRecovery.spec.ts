import { expect, test } from "@playwright/test";
import { holdDraftCommit } from "./holdDraftCommit.js";
import { locatorSchema } from "../src/features/operation-progress/locatorSchema.js";
import { parseOperation } from "../src/api/parseOperation.js";

test("SessionZero enables same-request recovery after a stalled acceptance deadline", async ({
  page,
}) => {
  await page.clock.install();
  let original = "";
  await page.route(
    "**/api/session-zero-drafts",
    async (route) => {
      const response = await route.fetch();
      original = parseOperation(await response.json()).operationId;
      // Withhold the real accepted response to exercise a stalled transport.
    },
    { times: 1 },
  );
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await expect.poll(() => original).not.toBe("");
  await page.clock.runFor(31_000);
  await expect(page.getByRole("status")).toContainText("Status unavailable");
  await expect(
    page.getByRole("button", { name: "Recover request" }),
  ).toHaveAttribute("aria-disabled", "false");
  await page.getByRole("button", { name: "Recover request" }).click();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
  expect(page.url()).toContain(original);
});

test("SessionZero resolves lost cancellation delivery from polling evidence", async ({
  page,
}) => {
  const barrier = await holdDraftCommit({ page });
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await barrier.reached();
  await expect(page.getByRole("status")).toContainText("Running");
  await page.route(
    "**/api/operations/*/cancel",
    async (route) => {
      expect((await route.fetch()).status()).toBe(200);
      await route.abort("failed");
    },
    { times: 1 },
  );
  await page.getByRole("button", { name: "Cancel start" }).click();
  await expect(page.getByRole("status")).toContainText(
    "Interrupted before commit",
  );
  await expect(
    page.getByRole("button", { name: "Retry draft" }),
  ).toHaveAttribute("aria-disabled", "false");
  await barrier.release();
});

test("SessionZero retires a stale rejected cancellation command", async ({
  page,
}) => {
  const barrier = await holdDraftCommit({ page });
  await page.route("**/api/operations/*/events", (route) =>
    route.abort("failed"),
  );
  await page.goto("http://127.0.0.1:5173");
  await page.getByRole("button", { name: "New Game" }).click();
  await barrier.reached();
  await expect(page.getByRole("status")).toContainText("Running");
  let releaseReads: () => void = () => {
    throw new Error("Read barrier is not initialized");
  };
  const held = new Promise<void>((resolve) => {
    releaseReads = resolve;
  });
  await page.route("**/api/operations/*", async (route) => {
    if (route.request().method() !== "GET") return route.continue();
    const response = await route.fetch();
    await held;
    await route.fulfill({ response });
  });
  const encoded = new URL(page.url()).searchParams.get("session0");
  if (!encoded) throw new Error("Missing locator");
  const payload: unknown = JSON.parse(encoded);
  const locator = locatorSchema.parse(payload);
  if (!locator.operationId) throw new Error("Missing operation identity");
  const response = await page.request.post(
    `http://127.0.0.1:8000/api/operations/${locator.operationId}/cancel`,
    {
      data: {
        requestId: `req_${crypto.randomUUID()}`,
        expectedLastEventId: locator.cursor,
      },
    },
  );
  expect(response.status()).toBe(200);
  await page.getByRole("button", { name: "Cancel start" }).click();
  await expect(page.getByRole("status")).toContainText(
    "Interrupted before commit",
  );
  await expect(
    page.getByRole("button", { name: "Recover request" }),
  ).toHaveCount(0);
  const refreshed: unknown = JSON.parse(
    new URL(page.url()).searchParams.get("session0") ?? "null",
  );
  expect(locatorSchema.parse(refreshed).recovery).toBeUndefined();
  releaseReads();
  await barrier.release();
  await page.reload();
  await page.getByRole("button", { name: "Retry draft" }).click();
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
});

test("App discards a recovery locator without operation coordinates", async ({
  page,
}) => {
  const locator = {
    requestId: "req_00000000-0000-4000-8000-000000000031",
    recovery: {
      action: "retry",
      requestId: "req_00000000-0000-4000-8000-000000000032",
      expectedLastEventId: 1,
    },
  };
  await page.goto(
    `http://127.0.0.1:5173/?session0=${encodeURIComponent(JSON.stringify(locator))}`,
  );
  await expect(page.getByRole("button", { name: "New Game" })).toBeVisible();
});

test("SessionZero preserves unresolved retry identity across refresh", async ({
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
    (route) => route.abort("failed"),
    { times: 1 },
  );
  await page.getByRole("button", { name: "Retry draft" }).click();
  await expect(page.getByRole("status")).toContainText("Status unavailable");
  const encoded = new URL(page.url()).searchParams.get("session0");
  if (!encoded) throw new Error("Missing recovery locator");
  const payload: unknown = JSON.parse(encoded);
  const original = locatorSchema.parse(payload);
  await page.reload();
  await expect(page.getByRole("status")).toContainText("Failed before commit");
  await expect(
    page.getByRole("button", { name: "Retry draft" }),
  ).toHaveAttribute("aria-disabled", "true");
  const submitted = page.waitForRequest(
    (request) =>
      request.url().endsWith("/retry") && request.method() === "POST",
  );
  await page.getByRole("button", { name: "Recover request" }).click();
  const sent: unknown = (await submitted).postDataJSON();
  expect(sent).toMatchObject({ requestId: original.recovery?.requestId });
  await expect(page.getByRole("status")).toContainText(
    "draft saved at revision 1",
  );
});
