import { operationSchema } from "./operationSchema.js";

/** Validate commit evidence before any UI use; for example, parseOperation(response.data). */
export function parseOperation(payload: unknown) {
  return operationSchema.parse(payload);
}
