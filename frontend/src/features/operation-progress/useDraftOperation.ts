import { useEffect, useRef, useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import type { Operation } from "../../api/generated/types.gen";
import { parseOperation } from "../../api/parseOperation";
import { selectOperationSnapshot } from "./selectOperationSnapshot";
import { readOperation } from "../../api/readOperation";
import { submitDraft } from "../../api/submitDraft";
import { recoverOperation } from "../../api/recoverOperation";
import { readLocator } from "./readLocator";
import { writeLocator } from "./writeLocator";
import { operationKey } from "./operationKey";
import { useOperationEvents } from "./useOperationEvents";
import type { OperationLocator } from "./locatorSchema";
import { operationLocator } from "./operationLocator";
import { recoveryOutcomeKnown } from "./recoveryOutcomeKnown";
import { rejectedRecoveryProblem } from "./rejectedRecoveryProblem";
import { contentUnavailableProblem } from "./contentUnavailableProblem";
import { clearLocator } from "./clearLocator";

/** Own explicit creation/recovery intent and query authoritative status; for example, useDraftOperation(). */
export function useDraftOperation() {
  const [locator, setLocator] = useState(readLocator);
  const [contentUnavailable, setContentUnavailable] = useState(false);
  const [starting, setStarting] = useState(false);
  const busy = useRef(false);
  const client = useQueryClient();
  const mutation = useMutation({
    retry: false,
    mutationFn: async (intent: OperationLocator) =>
      intent.recovery
        ? recoverOperation(intent)
        : submitDraft(intent.requestId),
    onSuccess: (operation) => {
      const prior = client.getQueryData<Operation>(
        operationKey(operationLocator(operation)),
      );
      const selected = selectOperationSnapshot(prior, operation);
      const updated = operationLocator(selected);
      writeLocator(updated);
      setLocator(updated);
      client.setQueryData<Operation>(operationKey(updated), selected);
    },
    onError: (error, intent) => {
      if (!intent.recovery && contentUnavailableProblem(error)) {
        clearLocator();
        setLocator(null);
        setContentUnavailable(true);
        return;
      }
      const problem = rejectedRecoveryProblem(error);
      if (!intent.recovery || !problem?.operation) return;
      const selected = selectOperationSnapshot(
        client.getQueryData<Operation>(operationKey(intent)),
        problem.operation,
      );
      const updated = operationLocator(selected);
      client.setQueryData<Operation>(operationKey(updated), selected);
      writeLocator(updated);
      setLocator(updated);
    },
    onSettled: () => {
      setStarting(false);
      busy.current = false;
    },
  });
  const query = useQuery({
    queryKey: operationKey(locator),
    enabled: !!locator?.operationId,
    retry: false,
    queryFn: ({ signal }) => {
      if (!locator?.operationId || !locator.draftId)
        throw new Error("No accepted operation");
      return readOperation({
        operationId: locator.operationId,
        requestId: locator.requestId,
        draftId: locator.draftId,
        signal,
      });
    },
    refetchInterval: (state) => {
      if (locator?.recovery) return 500;
      if (state.state.error) return 1000;
      const status = state.state.data?.status;
      return status === "complete" ||
        status === "failed" ||
        status === "interrupted"
        ? false
        : 500;
    },
    structuralSharing: (_oldData: unknown, newData: unknown) =>
      selectOperationSnapshot(
        client.getQueryData<Operation>(operationKey(locator)),
        parseOperation(newData),
      ),
  });
  const { isPending, reset } = mutation;
  useEffect(() => {
    if (!locator || !query.data) return;
    const resolved = !isPending && recoveryOutcomeKnown(locator, query.data);
    if (!resolved && query.data.lastEventId <= locator.cursor) return;
    const updated = resolved
      ? operationLocator(query.data)
      : { ...locator, cursor: query.data.lastEventId };
    writeLocator(updated);
    setLocator(updated);
    if (resolved) reset();
  }, [locator, query.data, isPending, reset]);
  useOperationEvents(locator);
  return {
    locator,
    contentUnavailable,
    starting,
    operation: query.data,
    unavailable:
      query.isError ||
      (mutation.isError &&
        !rejectedRecoveryProblem(mutation.error) &&
        !(locator && query.data && recoveryOutcomeKnown(locator, query.data))),
    pending: mutation.isPending,
    start: () => {
      if (busy.current || locator) return;
      busy.current = true;
      setContentUnavailable(false);
      setStarting(true);
      const intent: OperationLocator = {
        requestId: `req_${crypto.randomUUID()}`,
        cursor: 0,
      };
      writeLocator(intent);
      setLocator(intent);
      mutation.mutate(intent);
    },
    recoverRequest: () => {
      if (busy.current || !locator) return;
      busy.current = true;
      mutation.mutate(locator);
    },
    checkStatus: () => {
      mutation.reset();
      void query.refetch();
    },
    recover: (action: "retry" | "cancel") => {
      if (busy.current || !locator || locator.recovery || !query.data) return;
      busy.current = true;
      const intent: OperationLocator = {
        ...locator,
        recovery: {
          action,
          requestId: `req_${crypto.randomUUID()}`,
          expectedLastEventId: query.data.lastEventId,
        },
      };
      writeLocator(intent);
      setLocator(intent);
      mutation.mutate(intent);
    },
  };
}
