/** Forget a creation locator after a definitive rejection, since nothing exists to recover; for example, clearLocator(). */
export function clearLocator() {
  const url = new URL(window.location.href);
  url.searchParams.delete("session0");
  window.history.replaceState(null, "", url);
}
