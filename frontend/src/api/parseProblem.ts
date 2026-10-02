import { zProblem } from "./generated/zod.gen";
import { operationSchema } from "./operationSchema";

const problemSchema = zProblem
  .strict()
  .extend({
    operation: operationSchema.nullable().optional(),
    instance: zProblem.shape.instance.min(1),
    correlationId: zProblem.shape.correlationId.regex(/^cor_[a-f0-9-]{36}$/),
  })
  .refine((problem) => {
    const classification = {
      404: "not_found",
      409: "conflict",
      422: "invalid_input",
      503: "unavailable",
    }[problem.status];
    return (
      problem.classification === classification &&
      problem.instance === `urn:dmud:request:${problem.correlationId}`
    );
  }, "Inconsistent problem context");

/** Validate problem data without promoting malformed failures to known mutation outcomes; for example, parseProblem(error). */
export function parseProblem(payload: unknown) {
  return problemSchema.parse(payload);
}
