import { zGetSaveSlotsResponse } from "./generated/zod.gen";

const saveSlotsSchema = zGetSaveSlotsResponse
  .strict()
  .extend({ slots: zGetSaveSlotsResponse.shape.slots.element.strict().array() })
  .refine(
    ({ slots }) =>
      slots.length === 3 &&
      slots.every((slot, index) => slot.number === index + 1),
    "Expected exactly three ordered slots numbered 1 through 3",
  );

/** Validate the whole current save index before UI use; for example, parseSaveSlots(payload). */
export function parseSaveSlots(payload: unknown) {
  return saveSlotsSchema.parse(payload);
}
