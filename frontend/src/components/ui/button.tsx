import { cva, type VariantProps } from "class-variance-authority";
import type { ComponentProps } from "react";

const buttonStyles = cva(
  "min-h-11 min-w-[min(7rem,100%)] cursor-pointer rounded-md border border-amber px-4 py-[0.65rem] font-display text-button uppercase focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus disabled:cursor-not-allowed disabled:border-ink-muted disabled:bg-vellum disabled:text-ink-muted disabled:shadow-none max-[20rem]:w-full",
  {
    variants: {
      variant: {
        primary:
          "bg-amber text-on-amber shadow-[inset_0_0_0_3px_var(--color-amber),inset_0_0_0_4px_var(--color-on-amber)]",
        quiet: "bg-vellum text-amber",
      },
    },
    defaultVariants: { variant: "primary" },
  },
);

interface ButtonProps
  extends ComponentProps<"button">, VariantProps<typeof buttonStyles> {}

/**
 * Render a native button with campaign-book appearance and accessible focus states.
 * Defaults to a non-submitting button; form actions can explicitly use type="submit".
 * For example, <Button variant="quiet" onClick={openSheet}>Open character sheet</Button>.
 */
function Button(props: ButtonProps) {
  const { variant, className, type = "button", ...rest } = props;
  return (
    <button
      {...rest}
      type={type}
      className={buttonStyles({ variant, className })}
    />
  );
}

export default Button;
