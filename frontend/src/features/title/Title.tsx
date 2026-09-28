import { useSaveSlots } from "../../api/useSaveSlots";
import Button from "../../components/ui/button";
import Container from "../../components/ui/container";
import Heading from "../../components/ui/heading";
import Paragraph from "../../components/ui/paragraph";

interface TitleProps {
  onNewGame: () => void;
}

/** Show immediate campaign entry and truthful save discovery; for example, <Title onNewGame={start} />. */
function Title(props: TitleProps) {
  const { onNewGame } = props;
  const saves = useSaveSlots();

  let reason: string;
  if (saves.isPending || saves.isFetching) {
    reason = "Checking for saved campaigns…";
  } else if (saves.isError) {
    reason = "Saved campaigns could not be checked. Try again.";
  } else {
    reason = "No saved campaign exists.";
  }

  return (
    <Container as="section" aria-labelledby="title-heading">
      <Paragraph variant="eyebrow">A story in Brackenford</Paragraph>
      <Heading as="h1" id="title-heading" variant="title">
        dmud
      </Heading>
      <Paragraph variant="intro">A world awaits your first step.</Paragraph>
      <div className="mt-8 flex flex-wrap gap-3">
        <Button onClick={onNewGame}>New Game</Button>
        <Button aria-describedby="continue-reason" disabled variant="quiet">
          Continue
        </Button>
      </div>
      <Paragraph
        id="continue-reason"
        role={saves.isError && !saves.isFetching ? "alert" : "status"}
        variant={saves.isError && !saves.isFetching ? "alert" : "status"}
      >
        {reason}
      </Paragraph>
      {saves.errorUpdateCount > 0 && (
        <Button
          aria-describedby="continue-reason"
          aria-busy={saves.isFetching}
          aria-disabled={saves.isFetching}
          onClick={() => {
            if (!saves.isFetching) {
              void saves.refetch();
            }
          }}
          variant="quiet"
        >
          Retry save check
        </Button>
      )}
    </Container>
  );
}

export default Title;
