import { describe, expect, it } from "vitest";
import { parseStatus } from "./parseStatus";

describe("parseStatus", () => {
  it("accepts the declared ready response", () => {
    const payload: unknown = { status: "ready" };

    const result = parseStatus(payload);

    expect(result).toEqual({ status: "ready" });
  });

  it("rejects undeclared response fields", () => {
    const payload: unknown = { status: "ready", credential: "private" };

    expect(() => parseStatus(payload)).toThrow();
  });
});
