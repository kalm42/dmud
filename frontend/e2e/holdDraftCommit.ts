import { expect, type Page } from "@playwright/test";
import { zCreateSessionZeroDraft } from "../src/api/generated/zod.gen.js";

interface HoldDraftCommitArgs {
  page: Page;
  fail?: boolean;
}

/** Arm a test-composition barrier around the real worker; for example, holdDraftCommit({ page }). */
export async function holdDraftCommit(args: HoldDraftCommitArgs) {
  const { page, fail = false } = args;
  let requestId = "";
  await page.route(
    "**/api/session-zero-drafts",
    async (route) => {
      const payload: unknown = route.request().postDataJSON();
      const command = zCreateSessionZeroDraft.parse(payload);
      requestId = command.requestId;
      const response = await page.request.post(
        `http://127.0.0.1:8000/__test__/barriers/${requestId}?fail=${String(fail)}`,
      );
      expect(response.ok()).toBe(true);
      await route.continue();
    },
    { times: 1 },
  );
  return {
    reached: async () => {
      await expect
        .poll(async () => {
          if (!requestId) return false;
          const response = await page.request.get(
            `http://127.0.0.1:8000/__test__/barriers/${requestId}`,
          );
          const payload: unknown = await response.json();
          return (
            typeof payload === "object" &&
            payload !== null &&
            "reached" in payload &&
            payload.reached === true
          );
        })
        .toBe(true);
    },
    release: async () => {
      expect(
        (
          await page.request.post(
            `http://127.0.0.1:8000/__test__/barriers/${requestId}/release`,
          )
        ).ok(),
      ).toBe(true);
    },
  };
}
