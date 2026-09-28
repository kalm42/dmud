import { AxeBuilder } from "@axe-core/playwright";
import { expect, type Page } from "@playwright/test";

/** Scan the current page for detectable accessibility violations; for example, await expectAccessiblePage(page). */
export async function expectAccessiblePage(page: Page): Promise<void> {
  const result = await new AxeBuilder({ page }).analyze();
  expect(result.violations).toEqual([]);
}
