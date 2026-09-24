import { useStatus } from "../api/useStatus";
import { ZodError } from "zod";
import "./app.css";

/** Render the local startup shell; for example, <App />. */
function App() {
  const status = useStatus();

  return (
    <main className="shell">
      <div className="masthead">dmud</div>
      <section aria-labelledby="app-title" className="panel">
        <p className="eyebrow">Local application</p>
        <h1 id="app-title">A world is waiting</h1>
        <p>
          This foundation is running. Campaign play will arrive in a later
          story.
        </p>
        {status.isPending && <p role="status">Checking local API…</p>}
        {status.isError && (
          <p role="alert">
            {status.error instanceof ZodError ||
            status.error instanceof SyntaxError
              ? "The local API returned an unexpected response. Check the backend version and reload this page."
              : "The local API is unavailable. Start the backend and reload this page."}
          </p>
        )}
        {status.isSuccess && (
          <p role="status">Local API: {status.data.status}</p>
        )}
      </section>
    </main>
  );
}

export default App;
