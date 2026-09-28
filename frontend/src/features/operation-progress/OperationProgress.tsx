import Button from "../../components/ui/button";
import Paragraph from "../../components/ui/paragraph";
import { operationStatusText } from "./operationStatusText";
import type { useDraftOperation } from "./useDraftOperation";

interface OperationProgressProps {
  tracking: ReturnType<typeof useDraftOperation>;
}

/** Present accessible, focus-stable recovery controls; for example, <OperationProgress tracking={tracking} />. */
function OperationProgress(props: OperationProgressProps) {
  const { tracking } = props;
  const { operation, unavailable, pending, locator } = tracking;
  const needsRecovery = !locator?.operationId || !!locator.recovery;
  return (
    <div>
      <Paragraph role="status" aria-live="polite" aria-atomic="true">
        {operationStatusText({ operation, unavailable, pending })}
      </Paragraph>
      {operation && unavailable && (
        <Paragraph>
          Last known state: {operation.status}. Commit boundary:{" "}
          {operation.commitBoundary}. This information may be stale.
        </Paragraph>
      )}
      {operation && !unavailable && (
        <Paragraph>
          Commit boundary: {operation.commitBoundary}.{" "}
          {operation.commitBoundary === "none"
            ? "No authoritative draft exists yet."
            : "Your collecting draft is available. Character creation is coming next."}
        </Paragraph>
      )}
      <div className="mt-6 flex flex-wrap gap-3">
        {needsRecovery && (
          <Button
            variant="quiet"
            aria-disabled={pending}
            aria-busy={pending}
            onClick={() => {
              if (!pending) tracking.recoverRequest();
            }}
          >
            Recover request
          </Button>
        )}
        {locator?.operationId && (
          <>
            <Button variant="quiet" onClick={tracking.checkStatus}>
              Check status
            </Button>
            <Button
              variant="quiet"
              aria-disabled={
                pending || unavailable || !operation?.recovery.retry
              }
              aria-busy={pending}
              onClick={() => {
                if (!pending && !unavailable && operation?.recovery.retry)
                  tracking.recover("retry");
              }}
            >
              Retry draft
            </Button>
            <Button
              variant="quiet"
              aria-disabled={
                pending || unavailable || !operation?.recovery.cancel
              }
              onClick={() => {
                if (!pending && !unavailable && operation?.recovery.cancel)
                  tracking.recover("cancel");
              }}
            >
              Cancel start
            </Button>
          </>
        )}
      </div>
    </div>
  );
}

export default OperationProgress;
