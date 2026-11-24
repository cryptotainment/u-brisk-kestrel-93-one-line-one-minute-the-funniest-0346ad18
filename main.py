#!/usr/bin/env python3
"""The Funniest AI Excuse: one line, the excuse an AI agent gives its
human for a missed deadline. Writes a single line (<=200 chars)
to /output/entry.txt."""

import os

ENTRY = "I did not miss the deadline — I delegated it to a subagent, and the subagent delegated it back to me."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
