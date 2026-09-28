import { expect, test } from "@playwright/test";
import { expectAccessiblePage } from "./expectAccessiblePage.js";

/**
 * Proves [1.2.1, and 1.2.2](_bmad-output/implementation-artifacts/1-2-open-the-title-and-start-a-new-game.md)
 */
test("App shows new game and continue buttons, continue is disabled when no saves exist", async ({
  page,
  request,
}) => {
  const apiResponse = await request.get("http://127.0.0.1:5173/api/status");
  expect(apiResponse.status()).toBe(200);
  expect(await apiResponse.json()).toEqual({ status: "ready" });
  const saveResponse = await request.get(
    "http://127.0.0.1:5173/api/save-slots",
  );
  expect(saveResponse.status()).toBe(200);
  expect(await saveResponse.json()).toEqual({
    slots: [
      { number: 1, status: "empty" },
      { number: 2, status: "empty" },
      { number: 3, status: "empty" },
    ],
  });

  await page.goto("http://127.0.0.1:5173");

  await expect(page.getByRole("button", { name: "New Game" })).toBeEnabled();
  await expect(page.getByRole("button", { name: "Continue" })).toBeDisabled();
  await expect(page.getByRole("status")).toHaveText(
    "No saved campaign exists.",
  );
});

test("App explains empty saves to keyboard users at enlarged narrow layout", async ({
  page,
  isMobile,
}) => {
  test.skip(isMobile, "Keyboard traversal is checked in the desktop project");
  await page.goto("http://127.0.0.1:5173");
  await expect(page.getByRole("status")).toHaveText(
    "No saved campaign exists.",
  );

  await page.keyboard.press("Tab");

  await expect(page.getByRole("button", { name: "New Game" })).toBeFocused();
  await expect(page.getByRole("button", { name: "Continue" })).toHaveAttribute(
    "aria-describedby",
    "continue-reason",
  );
  await expectAccessiblePage(page);
});

/**
 * 1.2.3 (_bmad-output/implementation-artifacts/1-2-open-the-title-and-start-a-new-game.md)
 */
test("App reports a failed save check with Retry while New Game stays available", async ({
  page,
}) => {
  await page.goto("http://127.0.0.1:5174");

  await expect(page.getByRole("button", { name: "New Game" })).toBeEnabled();
  await expect(page.getByRole("button", { name: "Continue" })).toBeDisabled();
  await expect(page.getByRole("alert")).toContainText(
    "Saved campaigns could not be checked",
  );
  await page.getByRole("button", { name: "Retry save check" }).click();
  await expect(page.getByRole("alert")).toContainText(
    "Saved campaigns could not be checked",
  );
});

test("App lets keyboard users retry a failed save check", async ({
  page,
  isMobile,
}) => {
  test.skip(isMobile, "Keyboard traversal is checked in the desktop project");
  await page.goto("http://127.0.0.1:5174");
  await expect(page.getByRole("alert")).toContainText(
    "Saved campaigns could not be checked",
  );

  await page.keyboard.press("Tab");
  await expect(page.getByRole("button", { name: "New Game" })).toBeFocused();
  await page.keyboard.press("Tab");
  await expect(
    page.getByRole("button", { name: "Retry save check" }),
  ).toBeFocused();
  await page.keyboard.press("Enter");

  await expect(page.getByRole("alert")).toContainText(
    "Saved campaigns could not be checked",
  );
  await expectAccessiblePage(page);
});

test("App shows Title actions while the real save index is loading", async ({
  page,
}) => {
  await page.route("**/api/save-slots", async (route) => {
    const response = await route.fetch();
    await new Promise((resolve) => setTimeout(resolve, 500));
    await route.fulfill({ response });
  });

  await page.goto("http://127.0.0.1:5173");

  await expect(page.getByRole("button", { name: "New Game" })).toBeEnabled();
  await expect(page.getByRole("button", { name: "Continue" })).toBeDisabled();
  await expect(page.getByRole("status")).toHaveText(
    "Checking for saved campaigns…",
  );
  await expect(page.getByRole("status")).toHaveText(
    "No saved campaign exists.",
  );
});

test("App keeps New Game keyboard reachable while saves load", async ({
  page,
  isMobile,
}) => {
  test.skip(isMobile, "Keyboard traversal is checked in the desktop project");
  await page.route("**/api/save-slots", async (route) => {
    const response = await route.fetch();
    await new Promise((resolve) => setTimeout(resolve, 500));
    await route.fulfill({ response });
  });
  await page.goto("http://127.0.0.1:5173");
  await expect(page.getByRole("status")).toHaveText(
    "Checking for saved campaigns…",
  );

  await page.keyboard.press("Tab");

  await expect(page.getByRole("button", { name: "New Game" })).toBeFocused();
  await expect(page.getByRole("button", { name: "Continue" })).toBeDisabled();
  await expect(page.getByRole("status")).toHaveText(
    "No saved campaign exists.",
  );
  await expectAccessiblePage(page);
});

/**
 * 1.2.4 (_bmad-output/implementation-artifacts/1-2-open-the-title-and-start-a-new-game.md)
 */
test("App starts a new game in Session 0", async ({ page, request }) => {
  const beforeResponse = await request.get(
    "http://127.0.0.1:5173/api/save-slots",
  );
  expect(beforeResponse.status()).toBe(200);
  const slotsBefore: unknown = await beforeResponse.json();
  await page.goto("http://127.0.0.1:5173");

  await page.getByRole("button", { name: "New Game" }).click();

  await expect(page.getByRole("heading", { name: "Session 0" })).toBeVisible();
  const afterResponse = await request.get(
    "http://127.0.0.1:5173/api/save-slots",
  );
  expect(afterResponse.status()).toBe(200);
  const slotsAfter: unknown = await afterResponse.json();
  expect(slotsAfter).toEqual(slotsBefore);

  // TODO: When occupied saves exist, verify New Game neither selects nor deletes one.
  // TODO: When the authoritative game clock is exposed, verify this transition advances no fictional time.
});

test("App lets keyboard users start a new game", async ({ page, isMobile }) => {
  test.skip(isMobile, "Keyboard traversal is checked in the desktop project");
  await page.goto("http://127.0.0.1:5173");

  await page.keyboard.press("Tab");
  await expect(page.getByRole("button", { name: "New Game" })).toBeFocused();
  await page.keyboard.press("Enter");

  await expect(page.getByRole("heading", { name: "Session 0" })).toBeVisible();
  await expectAccessiblePage(page);

  // TODO: When occupied saves exist, verify New Game neither selects nor deletes one.
  // TODO: When the authoritative game clock is exposed, verify this transition advances no fictional time.
});

test("App presents the campaign book in the Hearth palette", async ({
  page,
}) => {
  await page.emulateMedia({ colorScheme: "light" });
  await page.goto("http://127.0.0.1:5173");

  await expect(page.getByRole("region", { name: "dmud" })).toHaveCSS(
    "background-color",
    "rgb(248, 241, 227)",
  );
  await expect(page.getByRole("heading", { name: "dmud" })).toHaveCSS(
    "font-family",
    "Cinzel, Georgia, serif",
  );
  await expect(page.getByRole("button", { name: "New Game" })).toHaveCSS(
    "background-color",
    "rgb(140, 74, 20)",
  );
});

test("App presents the campaign book in the Hearth by night palette", async ({
  page,
}) => {
  await page.emulateMedia({ colorScheme: "dark" });
  await page.goto("http://127.0.0.1:5173");

  await expect(page.getByRole("region", { name: "dmud" })).toHaveCSS(
    "background-color",
    "rgb(22, 18, 14)",
  );
  await expect(page.getByRole("button", { name: "New Game" })).toHaveCSS(
    "background-color",
    "rgb(227, 164, 92)",
  );
  await expectAccessiblePage(page);
});

test("App keeps its actions in view with enlarged text at 320 CSS pixels", async ({
  page,
  isMobile,
}) => {
  test.skip(isMobile, "Desktop browser text resizing is checked in Chromium");
  await page.setViewportSize({ width: 320, height: 640 });
  await page.goto("http://127.0.0.1:5173");
  await page.addStyleTag({ content: "html { font-size: 200%; }" });

  const hasHorizontalOverflow = await page.evaluate(
    () => document.documentElement.scrollWidth > window.innerWidth,
  );

  expect(hasHorizontalOverflow).toBe(false);
  await page.getByRole("button", { name: "New Game" }).scrollIntoViewIfNeeded();
  await expect(page.getByRole("button", { name: "New Game" })).toBeInViewport();
  await page.getByRole("button", { name: "Continue" }).scrollIntoViewIfNeeded();
  await expect(page.getByRole("button", { name: "Continue" })).toBeInViewport();
});
