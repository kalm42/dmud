import type { parseProblem } from "./parseProblem";

/** Retain validated recovery metadata across the adapter boundary. */
export class OperationProblem extends Error {
  readonly problem: ReturnType<typeof parseProblem>;

  constructor(problem: ReturnType<typeof parseProblem>) {
    super(problem.code);
    this.problem = problem;
  }
}
