import type { Page } from "@playwright/test";

interface HoldSaveCheckArgs {
  page: Page;
  forwardTo?: string;
}

/**
 * Hold delivery of a real save-index response until the caller releases it.
 * Optional forwarding exercises recovery through the available real API instead of the failed proxy.
 * For example, const release = await holdSaveCheck({ page }); await assertions(); release();
 */
export async function holdSaveCheck(
  args: HoldSaveCheckArgs,
): Promise<() => void> {
  const { page, forwardTo } = args;
  let release: () => void;
  const gate = new Promise<void>((resolve) => {
    release = resolve;
  });
  await page.route("**/api/save-slots", async (route) => {
    const response = await route.fetch(
      forwardTo === undefined ? {} : { url: forwardTo },
    );
    await gate;
    await route.fulfill({ response });
  });
  return () => {
    release();
  };
}
