import { getOperation } from "./generated/sdk.gen";
import { parseOperation } from "./parseOperation";
import { parseProblem } from "./parseProblem";

interface ReadOperationArgs {
  operationId: string;
  requestId: string;
  draftId: string;
  signal: AbortSignal;
}

/** Read a status scoped to the current subject; for example, readOperation(locatorWithSignal). */
export async function readOperation(args: ReadOperationArgs) {
  const { operationId, requestId, draftId, signal } = args;
  const response = await getOperation({ path: { operationId }, signal });
  if (response.error !== undefined)
    throw new Error(parseProblem(response.error).code);
  const operation = parseOperation(response.data);
  if (
    operation.operationId !== operationId ||
    operation.requestId !== requestId ||
    operation.subject.draftId !== draftId
  )
    throw new Error("Mismatched operation identity");
  return operation;
}
