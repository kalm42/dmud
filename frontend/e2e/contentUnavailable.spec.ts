import { expect, test } from "@playwright/test";
import { expectAccessiblePage } from "./expectAccessiblePage.js";

/**
 * Proves 1.4.4 (_bmad-output/implementation-artifacts/1-4-validate-the-authored-p0-starting-world.md)
 * against a real backend whose isolated content directory fails validation.
 */
const BROKEN = "http://127.0.0.1:5175";
const NOTICE =
  "The starting world could not be loaded, so no game was started.";

test("Title explains that invalid content prevented New Game", async ({
  page,
}) => {
  await page.goto(BROKEN);

  await page.getByRole("button", { name: "New Game" }).click();

  await expect(page.getByText(NOTICE)).toBeVisible();
  await expect(page.getByText(NOTICE)).toContainText("restart the application");
  await expect(page.getByRole("button", { name: "New Game" })).toBeEnabled();
});

test("Title keeps no recovery locator for a rejected New Game", async ({
  page,
}) => {
  await page.goto(BROKEN);

  await page.getByRole("button", { name: "New Game" }).click();
  await expect(page.getByText(NOTICE)).toBeVisible();

  expect(new URL(page.url()).searchParams.get("session0")).toBeNull();
  await expect(
    page.getByRole("button", { name: "Recover request" }),
  ).toHaveCount(0);
});

test("Title announces the content-unavailable state once, politely", async ({
  page,
}) => {
  await page.goto(BROKEN);

  await page.getByRole("button", { name: "New Game" }).click();
  await expect(page.getByText(NOTICE)).toBeVisible();

  await expect(
    page.locator('[aria-live="polite"]', { hasText: NOTICE }),
  ).toHaveCount(1);
  await expect(page.getByRole("alert")).toHaveCount(0);
});

test("Title preserves New Game keyboard focus when content fails", async ({
  page,
  isMobile,
}) => {
  test.skip(isMobile, "Keyboard traversal is checked in the desktop project");
  await page.goto(BROKEN);
  await page.keyboard.press("Tab");
  await page.keyboard.press("Enter");
  await expect(page.getByText(NOTICE)).toBeVisible();

  await expect(page.getByRole("button", { name: "New Game" })).toBeFocused();
  await expectAccessiblePage(page);
});

test("App creates no save when content is unavailable", async ({
  page,
  request,
}) => {
  const before: unknown = await (
    await request.get(`${BROKEN}/api/save-slots`)
  ).json();
  await page.goto(BROKEN);

  await page.getByRole("button", { name: "New Game" }).click();
  await expect(page.getByText(NOTICE)).toBeVisible();

  const after: unknown = await (
    await request.get(`${BROKEN}/api/save-slots`)
  ).json();
  expect(after).toEqual(before);
});
