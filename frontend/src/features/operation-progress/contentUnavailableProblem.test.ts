import { describe, expect, it } from "vitest";
import { OperationProblem } from "../../api/operationProblem";
import { parseProblem } from "../../api/parseProblem";
import { contentUnavailableProblem } from "./contentUnavailableProblem";

const correlationId = "cor_0199a0b2-7c1e-7d3a-9f00-1234567890ab";

function problem(code: string, status: number, classification: string) {
  return parseProblem({
    type: `urn:dmud:problem:${code}`,
    title: "Content unavailable",
    status,
    detail:
      "The authored starting world failed validation, so nothing was started.",
    code,
    classification,
    instance: `urn:dmud:request:${correlationId}`,
    correlationId,
    operation: null,
  });
}

describe("contentUnavailableProblem", () => {
  it("recognizes the typed content_unavailable rejection", () => {
    const error = new OperationProblem(
      problem("content_unavailable", 503, "unavailable"),
    );

    const result = contentUnavailableProblem(error);

    expect(result?.code).toBe("content_unavailable");
  });

  it("treats other unavailable problems as unknown outcomes", () => {
    const error = new OperationProblem(
      problem("operation_unavailable", 503, "unavailable"),
    );

    const result = contentUnavailableProblem(error);

    expect(result).toBeNull();
  });

  it("treats untyped transport failures as unknown outcomes", () => {
    const result = contentUnavailableProblem(new Error("content_unavailable"));

    expect(result).toBeNull();
  });

  it("rejects a content_unavailable problem with inconsistent classification", () => {
    expect(() => problem("content_unavailable", 503, "conflict")).toThrow();
  });
});
