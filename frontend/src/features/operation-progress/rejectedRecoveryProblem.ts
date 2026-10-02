import { OperationProblem } from "../../api/operationProblem";

/** Distinguish definitive recovery rejection from unknown delivery; for example, rejectedRecoveryProblem(error). */
export function rejectedRecoveryProblem(error: unknown) {
  if (!(error instanceof OperationProblem) || error.problem.status !== 409)
    return null;
  const { code } = error.problem;
  if (
    code === "stale_event" ||
    code === "recovery_not_supported" ||
    code === "draft_already_committed"
  )
    return error.problem;
  return null;
}
