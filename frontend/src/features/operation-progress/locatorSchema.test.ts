import { describe, expect, it } from "vitest";
import { locatorSchema } from "./locatorSchema";

const requestId = "req_00000000-0000-4000-8000-000000000031";

describe("locatorSchema", () => {
  it("accepts creation identity before acknowledgement", () => {
    expect(locatorSchema.safeParse({ requestId, cursor: 0 }).success).toBe(
      true,
    );
  });

  it("rejects recovery commands without operation identity", () => {
    expect(
      locatorSchema.safeParse({
        requestId,
        recovery: {
          action: "retry",
          requestId: "req_00000000-0000-4000-8000-000000000032",
          expectedLastEventId: 1,
        },
      }).success,
    ).toBe(false);
  });
});
