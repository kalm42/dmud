import { useState } from "react";
import SessionZero from "../features/session-zero/SessionZero";
import Title from "../features/title/Title";
import "./app.css";

/** Compose Title and Session 0 entry; for example, <App />. */
function App() {
  const [surface, setSurface] = useState<"title" | "session-zero">("title");

  return (
    <main className="shell">
      {surface === "title" ? (
        <Title
          onNewGame={() => {
            setSurface("session-zero");
          }}
        />
      ) : (
        <SessionZero />
      )}
    </main>
  );
}

export default App;
