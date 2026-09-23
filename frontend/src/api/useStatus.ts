import { useQuery } from "@tanstack/react-query";
import { getStatusOptions } from "./generated/@tanstack/react-query.gen";
import { getStatus } from "./generated/sdk.gen";
import { parseStatus } from "./parseStatus";

/** Load and validate backend readiness; for example, useStatus() inside App. */
export function useStatus() {
  return useQuery({
    ...getStatusOptions(),
    retry: false,
    queryFn: async () => {
      const response = await getStatus({ throwOnError: true });
      const payload: unknown = response.data;
      return parseStatus(payload);
    },
  });
}
