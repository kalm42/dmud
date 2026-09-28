import { useQuery } from "@tanstack/react-query";
import { getSaveSlotsOptions } from "./generated/@tanstack/react-query.gen";
import { getSaveSlots } from "./generated/sdk.gen";
import { parseSaveSlots } from "./parseSaveSlots";

/** Load a validated save index without hidden retries; for example, useSaveSlots() inside Title. */
export function useSaveSlots() {
  return useQuery({
    ...getSaveSlotsOptions(),
    retry: false,
    queryFn: async ({ signal }) => {
      const response = await getSaveSlots({ signal, throwOnError: true });
      const payload: unknown = response.data;
      return parseSaveSlots(payload);
    },
  });
}
