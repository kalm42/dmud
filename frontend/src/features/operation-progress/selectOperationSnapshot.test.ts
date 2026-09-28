import { describe, expect, it } from "vitest";
import { parseOperation } from "../../api/parseOperation";
import { selectOperationSnapshot } from "./selectOperationSnapshot";

const current = parseOperation({
  schemaVersion: 1,
  operationId: "op_00000000-0000-7000-8000-000000000001",
  requestId: "req_00000000-0000-4000-8000-000000000001",
  subject: {
    kind: "session_zero_draft",
    draftId: "draft_00000000-0000-7000-8000-000000000001",
  },
  status: "validating",
  commitBoundary: "none",
  committedRevision: null,
  lastEventId: 2,
  recovery: { retry: false, cancel: true },
  result: null,
  statusUrl: "/api/operations/op_00000000-0000-7000-8000-000000000001",
  eventsUrl: "/api/operations/op_00000000-0000-7000-8000-000000000001/events",
});

describe("selectOperationSnapshot", () => {
  it("keeps newer evidence when an old response arrives", () => {
    expect(
      selectOperationSnapshot(current, {
        ...current,
        status: "accepted",
        lastEventId: 1,
      }),
    ).toEqual(current);
  });
  it("ignores repeated event delivery", () => {
    expect(selectOperationSnapshot(current, { ...current })).toBe(current);
  });
  it("rejects a response for another subject", () => {
    expect(() =>
      selectOperationSnapshot(current, {
        ...current,
        subject: {
          ...current.subject,
          draftId: "draft_00000000-0000-7000-8000-000000000002",
        },
      }),
    ).toThrow();
  });
});
