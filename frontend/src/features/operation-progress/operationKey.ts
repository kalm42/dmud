import { getOperationQueryKey } from "../../api/generated/@tanstack/react-query.gen";
import type { OperationLocator } from "./locatorSchema";

/** Isolate status by request and subject in the server-state cache; for example, operationKey(locator). */
export function operationKey(locator: OperationLocator | null) {
  return [
    ...getOperationQueryKey({
      path: { operationId: locator?.operationId ?? "unknown" },
    }),
    locator?.requestId,
    locator?.draftId,
  ];
}
