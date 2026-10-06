import { createSessionZeroDraft } from "./generated/sdk.gen";
import { parseOperation } from "./parseOperation";
import { parseProblem } from "./parseProblem";
import { OperationProblem } from "./operationProblem";
import { operationDeadline } from "./operationDeadline";

/** Send or explicitly recover the original creation identity; for example, submitDraft(requestId). */
export async function submitDraft(requestId: string) {
  const deadline = operationDeadline();
  try {
    const response = await createSessionZeroDraft({
      signal: deadline.signal,
      body: {
        schemaVersion: 1,
        requestId,
        command: "create_session_zero_draft",
      },
    });
    if (response.error !== undefined)
      throw new OperationProblem(parseProblem(response.error));
    const operation = parseOperation(response.data);
    if (operation.requestId !== requestId)
      throw new Error("Mismatched creation identity");
    return operation;
  } finally {
    deadline.clear();
  }
}
