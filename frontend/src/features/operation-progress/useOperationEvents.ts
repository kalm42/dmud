import { useEffect, useRef } from "react";
import { useQueryClient } from "@tanstack/react-query";
import { getOperationEvents } from "../../api/generated/sdk.gen";
import { parseOperationEvent } from "../../api/parseOperationEvent";
import type { Operation } from "../../api/generated/types.gen";
import type { OperationLocator } from "./locatorSchema";
import { selectOperationSnapshot } from "./selectOperationSnapshot";
import { operationKey } from "./operationKey";

/** Consume validated replay while independent polling remains available; for example, useOperationEvents(locator). */
export function useOperationEvents(locator: OperationLocator | null) {
  const initialCursor = useRef(locator?.cursor ?? 0);
  const client = useQueryClient();
  const operationId = locator?.operationId;
  const requestId = locator?.requestId;
  const draftId = locator?.draftId;
  useEffect(() => {
    if (!operationId || !requestId || !draftId) return;
    const controller = new AbortController();
    const key = operationKey({ operationId, requestId, draftId, cursor: 0 });
    const cached = client.getQueryData<Operation>(key);
    void (async () => {
      try {
        const events = await getOperationEvents({
          path: { operationId },
          headers: {
            "Last-Event-ID": String(
              Math.max(cached?.lastEventId ?? 0, initialCursor.current),
            ),
          },
          signal: controller.signal,
          sseMaxRetryAttempts: 1,
        });
        for await (const payload of events.stream) {
          const event = parseOperationEvent(payload);
          if (
            event.operation.operationId !== operationId ||
            event.operation.requestId !== requestId ||
            event.operation.subject.draftId !== draftId
          )
            throw new Error("Mismatched event identity");
          if (controller.signal.aborted) return;
          client.setQueryData<Operation>(key, (prior) =>
            selectOperationSnapshot(prior, event.operation),
          );
        }
      } catch {
        // Polling independently recovers transport loss or invalid event data.
      }
    })();
    return () => {
      controller.abort();
    };
  }, [client, operationId, requestId, draftId]);
}
