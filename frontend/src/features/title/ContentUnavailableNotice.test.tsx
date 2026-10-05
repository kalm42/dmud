// @vitest-environment jsdom
import { cleanup, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";
import ContentUnavailableNotice from "./ContentUnavailableNotice";

afterEach(cleanup);

describe("ContentUnavailableNotice", () => {
  it("states that nothing was started and how to recover", () => {
    render(<ContentUnavailableNotice shown />);

    const notice = screen.getByText(/starting world could not be loaded/);

    expect(notice.textContent).toContain("no game was started");
    expect(notice.textContent).toContain("restart the application");
  });

  it("renders the notice inside a polite live region", () => {
    render(<ContentUnavailableNotice shown />);

    const region = screen
      .getByText(/starting world could not be loaded/)
      .closest("[aria-live]");

    expect(region?.getAttribute("aria-live")).toBe("polite");
  });

  it("keeps the live region mounted while hidden so later text is announced", () => {
    const { container } = render(<ContentUnavailableNotice shown={false} />);

    const region = container.querySelector('[aria-live="polite"]');

    expect(region?.textContent).toBe("");
  });

  it("does not take focus when shown", () => {
    const { rerender } = render(<ContentUnavailableNotice shown={false} />);

    rerender(<ContentUnavailableNotice shown />);

    expect(document.activeElement).toBe(document.body);
  });
});
