import { useDraftOperation } from "../features/operation-progress/useDraftOperation";
import SessionZero from "../features/session-zero/SessionZero";
import ContentUnavailableNotice from "../features/title/ContentUnavailableNotice";
import Title from "../features/title/Title";
import "./app.css";

/** Compose Title and Session 0 entry; for example, <App />. */
function App() {
  const tracking = useDraftOperation();

  return (
    <main className="shell">
      {!tracking.locator || tracking.starting ? (
        <Title
          starting={tracking.starting}
          onNewGame={() => {
            tracking.start();
          }}
        />
      ) : (
        <SessionZero tracking={tracking} />
      )}
      <ContentUnavailableNotice shown={tracking.contentUnavailable} />
    </main>
  );
}

export default App;
