import { cva, type VariantProps } from "class-variance-authority";
import type { ComponentProps } from "react";

const paragraphStyles = cva("my-[1em] text-interface", {
  variants: {
    variant: {
      body: null,
      eyebrow: "font-display text-label text-ink-muted uppercase",
      intro: "text-story",
      status: "border-l-4 border-amber bg-vellum-deep px-4 py-[0.6rem] italic",
      alert: "border-l-4 border-oxblood bg-vellum-deep px-4 py-[0.6rem]",
    },
  },
  defaultVariants: { variant: "body" },
});

interface ParagraphProps
  extends ComponentProps<"p">, VariantProps<typeof paragraphStyles> {}

/** Render a semantic paragraph with the Title's text styles; for example, <Paragraph variant="eyebrow">Chapter</Paragraph>. */
function Paragraph(props: ParagraphProps) {
  const { variant, className, ...rest } = props;
  return <p {...rest} className={paragraphStyles({ variant, className })} />;
}

export default Paragraph;
