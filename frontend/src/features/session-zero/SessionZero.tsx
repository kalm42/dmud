import { useEffect, useRef } from "react";
import OperationProgress from "../operation-progress/OperationProgress";
import type { useDraftOperation } from "../operation-progress/useDraftOperation";
import Container from "../../components/ui/container";
import Heading from "../../components/ui/heading";
import Paragraph from "../../components/ui/paragraph";

interface SessionZeroProps {
  tracking: ReturnType<typeof useDraftOperation>;
}

/** Introduce Session 0 without claiming any campaign data exists; for example, <SessionZero />. */
function SessionZero(props: SessionZeroProps) {
  const { tracking } = props;
  const heading = useRef<HTMLHeadingElement>(null);
  useEffect(() => {
    heading.current?.focus();
  }, []);

  return (
    <Container as="section" aria-labelledby="session-zero-heading">
      <Paragraph variant="eyebrow">New Game</Paragraph>
      <Heading
        as="h1"
        id="session-zero-heading"
        ref={heading}
        tabIndex={-1}
        className="focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus"
      >
        Session 0
      </Heading>
      <OperationProgress tracking={tracking} />
    </Container>
  );
}

export default SessionZero;
