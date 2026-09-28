import type { Operation } from "../../api/generated/types.gen";

/** Keep the newest validated snapshot of one identity; for example, selectOperationSnapshot(prior, incoming). */
export function selectOperationSnapshot(
  prior: Operation | undefined,
  incoming: Operation,
) {
  if (!prior) return incoming;
  if (
    prior.operationId !== incoming.operationId ||
    prior.requestId !== incoming.requestId ||
    prior.subject.draftId !== incoming.subject.draftId
  )
    throw new Error("Mismatched snapshot identity");
  return prior.lastEventId >= incoming.lastEventId ? prior : incoming;
}
