import { OperationProblem } from "../../api/operationProblem";

/** Recognize a definitive refusal to start because authored content is invalid; for example, contentUnavailableProblem(error). */
export function contentUnavailableProblem(error: unknown) {
  if (
    !(error instanceof OperationProblem) ||
    error.problem.code !== "content_unavailable" ||
    error.problem.status !== 503 ||
    error.problem.operation
  )
    return null;
  return error.problem;
}
