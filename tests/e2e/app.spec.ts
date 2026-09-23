import { expect, test } from "@playwright/test";

test("App shows readiness through the local API proxy", async ({
  page,
  request,
}) => {
  const apiResponse = await request.get("http://127.0.0.1:5173/api/status");
  expect(apiResponse.status()).toBe(200);
  expect(await apiResponse.json()).toEqual({ status: "ready" });

  await page.goto("http://127.0.0.1:5173");

  await expect(
    page.getByRole("heading", { name: "A world is waiting" }),
  ).toBeVisible();
  await expect(page.getByRole("status")).toHaveText("Local API: ready");
});

test("App explains when the local API is unavailable", async ({ page }) => {
  await page.goto("http://127.0.0.1:5174");

  await expect(page.getByRole("alert")).toContainText(
    "The local API is unavailable",
  );
});

test("App keeps the backend canary out of browser-visible surfaces", async ({
  page,
  request,
}) => {
  const responses = await Promise.all([
    request.get("http://127.0.0.1:5173/"),
    request.get("http://127.0.0.1:5173/src/main.tsx"),
    request.get("http://127.0.0.1:5173/api/status"),
  ]);
  const texts = await Promise.all(responses.map((response) => response.text()));

  await page.goto("http://127.0.0.1:5173");
  await expect(page.getByRole("status")).toHaveText("Local API: ready");
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
  ).not.toContain("canary-private-credential-123");
});
