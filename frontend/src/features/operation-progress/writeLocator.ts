import { locatorSchema, type OperationLocator } from "./locatorSchema";

/** Preserve only validated recovery coordinates before sending; for example, writeLocator(locator). */
export function writeLocator(locator: OperationLocator) {
  const validated = locatorSchema.parse(locator);
  const url = new URL(window.location.href);
  url.searchParams.set("session0", JSON.stringify(validated));
  window.history.replaceState(null, "", url);
}
