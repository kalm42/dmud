import {
  zDraftResult,
  zOperation,
  zRecoveryCapability,
  zSubject,
} from "./generated/zod.gen.js";

export const operationSchema = zOperation
  .strict()
  .extend({
    schemaVersion: zOperation.shape.schemaVersion.unwrap().nonoptional(),
    subject: zSubject
      .strict()
      .extend({ kind: zSubject.shape.kind.unwrap().nonoptional() }),
    recovery: zRecoveryCapability.strict(),
    result: zDraftResult
      .strict()
      .extend({
        subject: zSubject
          .strict()
          .extend({ kind: zSubject.shape.kind.unwrap().nonoptional() }),
        commitBoundary: zDraftResult.shape.commitBoundary
          .unwrap()
          .nonoptional(),
      })
      .nullable(),
  })
  .refine((operation) => {
    const committed = operation.commitBoundary === "draft";
    if (
      committed !==
      (operation.status === "committed" || operation.status === "complete")
    )
      return false;
    if (
      committed !== (operation.result !== null) ||
      committed !== (operation.committedRevision !== null)
    )
      return false;
    if (
      operation.result &&
      (operation.result.subject.draftId !== operation.subject.draftId ||
        operation.result.committedRevision !== operation.committedRevision)
    )
      return false;
    if (
      operation.recovery.retry !==
      (operation.status === "failed" || operation.status === "interrupted")
    )
      return false;
    if (
      operation.recovery.cancel !==
      (operation.status === "accepted" || operation.status === "validating")
    )
      return false;
    return (
      operation.statusUrl === `/api/operations/${operation.operationId}` &&
      operation.eventsUrl === `${operation.statusUrl}/events`
    );
  }, "Inconsistent operation evidence");
