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

/** Own explicit creation/recovery intent and query authoritative status; for example, useDraftOperation(). */
export function useDraftOperation() {
  const [locator, setLocator] = useState(readLocator);
  const busy = useRef(false);
  const client = useQueryClient();
  const mutation = useMutation({
    retry: false,
    mutationFn: async (intent: OperationLocator) =>
      intent.recovery
        ? recoverOperation(intent)
        : submitDraft(intent.requestId),
    onSuccess: (operation) => {
      const updated: OperationLocator = {
        requestId: operation.requestId,
        operationId: operation.operationId,
        draftId: operation.subject.draftId,
        cursor: operation.lastEventId,
      };
      writeLocator(updated);
      setLocator(updated);
      client.setQueryData<Operation>(operationKey(updated), (prior) =>
        selectOperationSnapshot(prior, operation),
      );
    },
    onSettled: () => {
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
  useEffect(() => {
    if (!locator || !query.data || query.data.lastEventId <= locator.cursor)
      return;
    const updated = { ...locator, cursor: query.data.lastEventId };
    writeLocator(updated);
    setLocator(updated);
  }, [locator, query.data]);
  useOperationEvents(locator);
  return {
    locator,
    operation: query.data,
    unavailable: query.isError || mutation.isError,
    pending: mutation.isPending,
    start: () => {
      if (busy.current || locator) return;
      busy.current = true;
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
      if (busy.current || !locator || !query.data) return;
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
