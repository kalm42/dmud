import { expect, test } from "@playwright/test";

test("App keeps the backend canary out of browser-visible surfaces", async ({
  page,
  request,
}) => {
  const canary = process.env.DMUD_TEST_CANARY;
  if (canary === undefined) {
    throw new Error("Playwright did not provide the test credential canary");
  }
  const responses = await Promise.all([
    request.get("http://127.0.0.1:5173/"),
    request.get("http://127.0.0.1:5173/src/main.tsx"),
    request.get("http://127.0.0.1:5173/playwright.config.ts"),
    request.get("http://127.0.0.1:5173/api/status"),
    request.get("http://127.0.0.1:5173/api/save-slots"),
  ]);
  const texts = await Promise.all(responses.map((response) => response.text()));
  await page.goto("http://127.0.0.1:5173");
  await expect(page.getByRole("status")).toHaveText(
    "No saved campaign exists.",
  );

  const storage = await page.evaluate(() => ({
    local: JSON.stringify(localStorage),
    session: JSON.stringify(sessionStorage),
  }));

  expect(
    [
      ...texts,
      await page.locator("body").innerText(),
      ...Object.values(storage),
    ].join(" "),
  ).not.toContain(canary);
});
