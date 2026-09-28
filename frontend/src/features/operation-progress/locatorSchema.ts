import { z } from "zod";
import { zOperation, zRecoveryCommand } from "../../api/generated/zod.gen";

export const locatorSchema = z
  .object({
    requestId: zOperation.shape.requestId,
    operationId: zOperation.shape.operationId.optional(),
    draftId: zOperation.shape.subject.shape.draftId.optional(),
    cursor: z.number().int().nonnegative().default(0),
    recovery: z
      .object({
        action: z.enum(["retry", "cancel"]),
        requestId: zRecoveryCommand.shape.requestId,
        expectedLastEventId: zRecoveryCommand.shape.expectedLastEventId,
      })
      .strict()
      .optional(),
  })
  .strict()
  .refine(
    (locator) =>
      (locator.operationId === undefined) === (locator.draftId === undefined),
  );
export type OperationLocator = z.infer<typeof locatorSchema>;
