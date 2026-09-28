import { describe, expect, it } from "vitest";
import { parseSaveSlots } from "./parseSaveSlots";

describe("parseSaveSlots", () => {
  it("accepts the three numbered empty slots", () => {
    const payload: unknown = {
      slots: [1, 2, 3].map((number) => ({ number, status: "empty" })),
    };

    expect(parseSaveSlots(payload)).toEqual(payload);
  });

  it("rejects an omitted slot", () => {
    const payload: unknown = { slots: [{ number: 1, status: "empty" }] };

    expect(() => parseSaveSlots(payload)).toThrow();
  });

  it("rejects an undeclared occupied slot", () => {
    const payload: unknown = {
      slots: [
        { number: 1, status: "occupied" },
        { number: 2, status: "empty" },
        { number: 3, status: "empty" },
      ],
    };

    expect(() => parseSaveSlots(payload)).toThrow();
  });

  it("rejects extra fields inside a slot", () => {
    const payload: unknown = {
      slots: [
        { number: 1, status: "empty", secret: "private" },
        { number: 2, status: "empty" },
        { number: 3, status: "empty" },
      ],
    };

    expect(() => parseSaveSlots(payload)).toThrow();
  });
});
