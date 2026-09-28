import { cva } from "class-variance-authority";
import type { HTMLAttributes } from "react";

const containerStyles = cva(
  "relative w-[min(100%,42rem)] min-w-0 rounded-sm border border-gilt bg-vellum p-[clamp(1.5rem,6vw,3rem)] wrap-anywhere shadow-page before:pointer-events-none before:absolute before:inset-[0.35rem] before:rounded-[2px] before:border before:border-gilt before:content-['']",
);

interface ContainerProps extends HTMLAttributes<HTMLElement> {
  as?: "div" | "section" | "article" | "aside";
}

/**
 * Frame a campaign-book surface with responsive padding and an inset gilt border.
 * Choose a semantic element and provide its accessible label where appropriate.
 * For example, <Container as="section" aria-labelledby="title-heading">...</Container>.
 */
function Container(props: ContainerProps) {
  const { as: Tag = "div", className, ...rest } = props;
  return <Tag {...rest} className={containerStyles({ className })} />;
}

export default Container;
