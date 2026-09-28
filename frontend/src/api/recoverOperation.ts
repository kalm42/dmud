import { cancelOperation, retryOperation } from "./generated/sdk.gen";
import { parseOperation } from "./parseOperation";
import { parseProblem } from "./parseProblem";
import type { OperationLocator } from "../features/operation-progress/locatorSchema";

/** Repeat a persisted recovery command safely after response loss; for example, recoverOperation(locator). */
export async function recoverOperation(locator: OperationLocator) {
  const { operationId, recovery, requestId, draftId } = locator;
  if (!operationId || !recovery) throw new Error("No recovery identity");
  const options = {
    path: { operationId },
    body: {
      schemaVersion: 1,
      requestId: recovery.requestId,
      expectedLastEventId: recovery.expectedLastEventId,
    },
  } satisfies Parameters<typeof retryOperation>[0];
  const response = await (recovery.action === "retry"
    ? retryOperation(options)
    : cancelOperation(options));
  if (response.error !== undefined)
    throw new Error(parseProblem(response.error).code);
  const operation = parseOperation(response.data);
  if (
    operation.operationId !== operationId ||
    operation.requestId !== requestId ||
    operation.subject.draftId !== draftId
  )
    throw new Error("Mismatched recovery identity");
  return operation;
}
