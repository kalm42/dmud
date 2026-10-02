import { locatorSchema } from "./locatorSchema";

/** Read a non-authoritative URL locator without trusting it as game state; for example, readLocator(). */
export function readLocator() {
  const encoded = new URL(window.location.href).searchParams.get("session0");
  if (!encoded) return null;
  try {
    const payload: unknown = JSON.parse(encoded);
    const parsed = locatorSchema.safeParse(payload);
    return parsed.success ? parsed.data : null;
  } catch {
    return null;
  }
}
