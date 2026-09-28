import { useDraftOperation } from "../features/operation-progress/useDraftOperation";
import SessionZero from "../features/session-zero/SessionZero";
import Title from "../features/title/Title";
import "./app.css";

/** Compose Title and Session 0 entry; for example, <App />. */
function App() {
  const tracking = useDraftOperation();

  return (
    <main className="shell">
      {!tracking.locator ? (
        <Title
          onNewGame={() => {
            tracking.start();
          }}
        />
      ) : (
        <SessionZero tracking={tracking} />
      )}
    </main>
  );
}

export default App;
