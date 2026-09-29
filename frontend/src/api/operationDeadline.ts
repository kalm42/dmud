/** Bound unknown mutation transport without cancelling server work; for example, operationDeadline(). */
export function operationDeadline() {
  const controller = new AbortController();
  const timer = window.setTimeout(() => {
    controller.abort();
  }, 30_000);
  return {
    signal: controller.signal,
    clear: () => {
      window.clearTimeout(timer);
    },
  };
}
