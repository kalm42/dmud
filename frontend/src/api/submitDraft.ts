import { createSessionZeroDraft } from "./generated/sdk.gen";
import { parseOperation } from "./parseOperation";
import { parseProblem } from "./parseProblem";

/** Send or explicitly recover the original creation identity; for example, submitDraft(requestId). */
export async function submitDraft(requestId: string) {
  const response = await createSessionZeroDraft({
    body: { schemaVersion: 1, requestId, command: "create_session_zero_draft" },
  });
  if (response.error !== undefined)
    throw new Error(parseProblem(response.error).code);
  const operation = parseOperation(response.data);
  if (operation.requestId !== requestId)
    throw new Error("Mismatched creation identity");
  return operation;
}
