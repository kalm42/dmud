import { zGetStatusResponse } from "./generated/zod.gen";

/** Validate the API response before UI use; for example, parseStatus({ status: 'ready' }). */
export function parseStatus(payload: unknown) {
  return zGetStatusResponse.strict().parse(payload);
}
