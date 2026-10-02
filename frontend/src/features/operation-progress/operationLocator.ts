import type { Operation } from "../../api/generated/types.gen";
import type { OperationLocator } from "./locatorSchema";

/** Derive identifiers from validated authoritative evidence; for example, operationLocator(operation). */
export function operationLocator(operation: Operation): OperationLocator {
  return {
    requestId: operation.requestId,
    operationId: operation.operationId,
    draftId: operation.subject.draftId,
    cursor: operation.lastEventId,
  };
}
