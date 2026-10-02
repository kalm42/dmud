import { zOperationEvent } from "./generated/zod.gen";
import { operationSchema } from "./operationSchema";

const eventSchema = zOperationEvent
  .strict()
  .extend({
    schemaVersion: zOperationEvent.shape.schemaVersion.unwrap().nonoptional(),
    operation: operationSchema,
  })
  .refine(
    (event) => event.eventId === event.operation.lastEventId,
    "Event cursor differs from snapshot",
  );

/** Validate SSE data with the generated event schema; for example, parseOperationEvent(data). */
export function parseOperationEvent(payload: unknown) {
  return eventSchema.parse(payload);
}
