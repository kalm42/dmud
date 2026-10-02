import type { Operation } from "../../api/generated/types.gen";

interface OperationStatusArgs {
  operation?: Operation;
  unavailable: boolean;
  pending: boolean;
}

/** Describe only evidenced status and boundary; for example, operationStatusText({ operation, unavailable: false, pending: false }). */
export function operationStatusText(args: OperationStatusArgs) {
  const { operation, unavailable, pending } = args;
  if (unavailable)
    return "Status unavailable. The current outcome is unknown; recover the original request or check status again.";
  if (!operation) {
    if (pending)
      return "Starting Session 0… Awaiting durable acceptance. No draft commit is acknowledged.";
    return "Request outcome unknown. Recover the original request to check whether it was accepted.";
  }
  switch (operation.status) {
    case "accepted":
      return "Accepted. Session 0 start is recorded; no draft has committed yet.";
    case "validating":
      return "Running. Preparing Session 0; no draft has committed yet.";
    case "committed":
      return `Draft committed at revision ${String(operation.committedRevision)}. Completing delivery…`;
    case "complete":
      return `Complete. Session 0 draft saved at revision ${String(operation.committedRevision)}.`;
    case "failed":
      return "Failed before commit. No draft was saved. You can retry this draft.";
    case "interrupted":
      return "Interrupted before commit. No draft was saved. You can retry this draft.";
  }
}
