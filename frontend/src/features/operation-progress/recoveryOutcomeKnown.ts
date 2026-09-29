import type { Operation } from "../../api/generated/types.gen";
import type { OperationLocator } from "./locatorSchema";

/** Resolve uncertain delivery only from newer matching evidence; for example, recoveryOutcomeKnown(locator, operation). */
export function recoveryOutcomeKnown(
  locator: OperationLocator,
  operation: Operation,
) {
  const { recovery } = locator;
  if (
    !recovery ||
    operation.operationId !== locator.operationId ||
    operation.requestId !== locator.requestId ||
    operation.subject.draftId !== locator.draftId ||
    operation.lastEventId <= recovery.expectedLastEventId
  )
    return false;
  if (recovery.action === "retry") return true;
  return (
    operation.status === "interrupted" ||
    operation.status === "committed" ||
    operation.status === "complete"
  );
}
