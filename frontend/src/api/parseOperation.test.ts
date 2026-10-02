import { describe, expect, it } from "vitest";
import { parseOperation } from "./parseOperation";

const operation = {
  schemaVersion: 1,
  operationId: "op_00000000-0000-7000-8000-000000000001",
  requestId: "req_00000000-0000-4000-8000-000000000001",
  subject: {
    kind: "session_zero_draft",
    draftId: "draft_00000000-0000-7000-8000-000000000001",
  },
  status: "accepted",
  commitBoundary: "none",
  committedRevision: null,
  lastEventId: 1,
  recovery: { retry: false, cancel: true },
  result: null,
  statusUrl: "/api/operations/op_00000000-0000-7000-8000-000000000001",
  eventsUrl: "/api/operations/op_00000000-0000-7000-8000-000000000001/events",
};

describe("parseOperation", () => {
  it("accepts an uncommitted operation", () => {
    expect(parseOperation(operation)).toEqual(operation);
  });
  it("rejects a complete operation without commit evidence", () => {
    expect(() =>
      parseOperation({ ...operation, status: "complete" }),
    ).toThrow();
  });
  it("rejects unknown nested fields", () => {
    expect(() =>
      parseOperation({
        ...operation,
        subject: { ...operation.subject, campaign: "invented" },
      }),
    ).toThrow();
  });
  it("rejects an inconsistent subject result", () => {
    expect(() =>
      parseOperation({
        ...operation,
        status: "complete",
        commitBoundary: "draft",
        committedRevision: 1,
        result: {
          subject: {
            ...operation.subject,
            draftId: "draft_00000000-0000-7000-8000-000000000002",
          },
          commitBoundary: "draft",
          committedRevision: 1,
        },
      }),
    ).toThrow();
  });
});

// These boundaries must reject data before any authoritative status is rendered.
describe("parseOperationEvent", () => {
  it("rejects mismatched event cursors", async () => {
    const { parseOperationEvent } = await import("./parseOperationEvent");
    expect(() =>
      parseOperationEvent({ schemaVersion: 1, eventId: 2, operation }),
    ).toThrow();
  });
  it("rejects malformed event snapshots", async () => {
    const { parseOperationEvent } = await import("./parseOperationEvent");
    expect(() =>
      parseOperationEvent({
        schemaVersion: 1,
        eventId: 1,
        operation: { ...operation, status: "complete" },
      }),
    ).toThrow();
  });
});

describe("parseProblem", () => {
  it("rejects malformed authoritative metadata", async () => {
    const { parseProblem } = await import("./parseProblem");
    expect(() =>
      parseProblem({
        type: "urn:dmud:problem:conflict",
        title: "Conflict",
        status: 409,
        detail: "Recover",
        code: "request_conflict",
        classification: "conflict",
        correlationId: "cor_00000000-0000-7000-8000-000000000001",
        instance: "urn:dmud:request:cor_00000000-0000-7000-8000-000000000001",
        operation: { ...operation, committedRevision: 1 },
      }),
    ).toThrow();
  });
});
