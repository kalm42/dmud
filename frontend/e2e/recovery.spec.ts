import { expect, test } from "@playwright/test";
import { expectAccessiblePage } from "./expectAccessiblePage.js";
import { holdSaveCheck } from "./holdSaveCheck.js";

test("Title recovers save discovery through the real available API", async ({
  page,
}) => {
  await page.goto("http://127.0.0.1:5174");
  await expect(page.getByRole("alert")).toContainText(
    "Saved campaigns could not be checked",
  );
  const release = await holdSaveCheck({
    page,
    forwardTo: "http://127.0.0.1:5173/api/save-slots",
  });

  await page.getByRole("button", { name: "Retry save check" }).click();

  await expect(page.getByRole("status")).toHaveText(
    "Checking for saved campaigns…",
  );
  release();
  await expect(page.getByRole("status")).toHaveText(
    "No saved campaign exists.",
  );
  await expect(page.getByRole("button", { name: "Continue" })).toBeDisabled();
  await expect(page.getByRole("button", { name: "New Game" })).toBeEnabled();
});

test("Title preserves keyboard focus through recovery at enlarged narrow layout", async ({
  page,
  isMobile,
}) => {
  test.skip(isMobile, "Keyboard traversal is checked in the desktop project");
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.setViewportSize({ width: 320, height: 640 });
  await page.goto("http://127.0.0.1:5174");
  await page.addStyleTag({ content: "html { font-size: 200%; }" });
  await expect(page.getByRole("alert")).toBeVisible();
  const release = await holdSaveCheck({
    page,
    forwardTo: "http://127.0.0.1:5173/api/save-slots",
  });
  await page.keyboard.press("Tab");
  await page.keyboard.press("Tab");
  const retry = page.getByRole("button", { name: "Retry save check" });
  await expect(retry).toBeFocused();
  await expect(retry).toHaveCSS("outline-style", "solid");
  await expect(retry).toHaveCSS("outline-width", "2px");

  await page.keyboard.press("Enter");

  await expect(page.getByRole("status")).toHaveText(
    "Checking for saved campaigns…",
  );
  await expect(retry).toBeFocused();
  await expect(retry).toHaveAttribute("aria-disabled", "true");
  release();
  await expect(page.getByRole("status")).toHaveText(
    "No saved campaign exists.",
  );
  await expect(retry).toBeFocused();
  await expect(retry).toHaveAttribute("aria-disabled", "false");
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth > window.innerWidth,
    ),
  ).toBe(false);
  for (const name of ["New Game", "Continue", "Retry save check"]) {
    const bounds = await page.getByRole("button", { name }).boundingBox();
    expect(bounds).not.toBeNull();
    expect(bounds?.width).toBeGreaterThanOrEqual(24);
    expect(bounds?.height).toBeGreaterThanOrEqual(24);
  }
  await expectAccessiblePage(page);
  await page.keyboard.press("Shift+Tab");
  await expect(page.getByRole("button", { name: "New Game" })).toBeFocused();
  await page.keyboard.press("Enter");
  await expect(page.getByRole("heading", { name: "Session 0" })).toBeFocused();
});
