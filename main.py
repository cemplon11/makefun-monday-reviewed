"""Monday, Reviewed in One Line.

Writes a single one-line product-style review of Monday to
/output/entry.txt. Pure standard library, fully deterministic:
the same line is produced on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def build_review() -> str:
    """Assemble the review from its parts, like a bad delivery manifest."""
    rating = "One star."
    inbox = "Monday shipped 43 unread emails"
    sync = "a 58-minute 'quick sync'"
    invite = "and a meeting booked by my past self"
    verdict = "Worst subscription ever"
    twist = "and it auto-renews every week"
    parts = [rating, inbox + ",", sync + ",", invite + ".", verdict, "—", twist + "."]
    return " ".join(parts)


def main() -> None:
    line = build_review()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
