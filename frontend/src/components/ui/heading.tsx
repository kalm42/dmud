import { cva, type VariantProps } from "class-variance-authority";
import type { ComponentProps } from "react";

const headingStyles = cva("mt-2 mb-6 font-display text-ink", {
  variants: {
    variant: {
      title: "text-title max-sm:text-[clamp(2rem,8vw,var(--text-title))]",
      scene: "text-scene-title",
      overlay: "text-overlay-title",
      label: "text-label",
    },
  },
  defaultVariants: { variant: "scene" },
});

interface HeadingProps
  extends ComponentProps<"h1">, VariantProps<typeof headingStyles> {
  as?: "h1" | "h2" | "h3" | "h4" | "h5" | "h6";
}

/**
 * Render a semantic heading with campaign-book typography.
 * Choose the heading level separately from its visual variant to preserve document order.
 * For example, <Heading as="h1" variant="title">dmud</Heading>.
 */
function Heading(props: HeadingProps) {
  const { as: Tag = "h2", variant, className, ...rest } = props;
  return <Tag {...rest} className={headingStyles({ variant, className })} />;
}

export default Heading;
