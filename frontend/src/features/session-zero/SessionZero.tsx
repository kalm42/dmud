import { useEffect, useRef } from "react";
import Container from "../../components/ui/container";
import Heading from "../../components/ui/heading";
import Paragraph from "../../components/ui/paragraph";

/** Introduce Session 0 without claiming any campaign data exists; for example, <SessionZero />. */
function SessionZero() {
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
      <Paragraph>
        Your journey begins here. Character creation is coming next.
      </Paragraph>
    </Container>
  );
}

export default SessionZero;
