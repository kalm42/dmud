import Container from "../../components/ui/container";
import Heading from "../../components/ui/heading";
import Paragraph from "../../components/ui/paragraph";

/** Introduce Session 0 without claiming any campaign data exists; for example, <SessionZero />. */
function SessionZero() {
  return (
    <Container as="section" aria-labelledby="session-zero-heading">
      <Paragraph variant="eyebrow">New Game</Paragraph>
      <Heading as="h1" id="session-zero-heading">
        Session 0
      </Heading>
      <Paragraph>
        Your journey begins here. Character creation is coming next.
      </Paragraph>
    </Container>
  );
}

export default SessionZero;
