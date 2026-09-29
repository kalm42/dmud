import { cancelOperation, retryOperation } from "./generated/sdk.gen";
import { parseOperation } from "./parseOperation";
import { parseProblem } from "./parseProblem";
import { OperationProblem } from "./operationProblem";
import { operationDeadline } from "./operationDeadline";
import type { OperationLocator } from "../features/operation-progress/locatorSchema";

/** Repeat a persisted recovery command safely after response loss; for example, recoverOperation(locator). */
export async function recoverOperation(locator: OperationLocator) {
  const { operationId, recovery, requestId, draftId } = locator;
  if (!operationId || !recovery) throw new Error("No recovery identity");
  const deadline = operationDeadline();
  try {
    const options = {
      signal: deadline.signal,
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
    if (response.error !== undefined) {
      const problem = parseProblem(response.error);
      if (
        problem.operation &&
        (problem.operation.operationId !== operationId ||
          problem.operation.requestId !== requestId ||
          problem.operation.subject.draftId !== draftId)
      )
        throw new Error("Mismatched recovery problem identity");
      throw new OperationProblem(problem);
    }
    const operation = parseOperation(response.data);
    if (
      operation.operationId !== operationId ||
      operation.requestId !== requestId ||
      operation.subject.draftId !== draftId
    )
      throw new Error("Mismatched recovery identity");
    return operation;
  } finally {
    deadline.clear();
  }
}
