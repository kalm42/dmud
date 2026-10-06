import Paragraph from "../../components/ui/paragraph";

interface ContentUnavailableNoticeProps {
  shown: boolean;
}

/**
 * Keep one polite live region mounted across Title and Session 0 so the factual
 * content-unavailable state is announced once when it appears, without moving focus.
 * For example, <ContentUnavailableNotice shown={tracking.contentUnavailable} />.
 */
function ContentUnavailableNotice(props: ContentUnavailableNoticeProps) {
  const { shown } = props;
  return (
    <div aria-live="polite" aria-atomic="true" className="w-[min(100%,42rem)]">
      {shown && (
        <Paragraph variant="alert">
          The starting world could not be loaded, so no game was started. Fix
          the game content and restart the application, then choose New Game
          again.
        </Paragraph>
      )}
    </div>
  );
}

export default ContentUnavailableNotice;
