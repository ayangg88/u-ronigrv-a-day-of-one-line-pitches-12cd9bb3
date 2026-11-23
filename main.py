#!/usr/bin/env python3
"""One-line pitch entry for make.fun's A Day of One-Line Pitches.

Writes a single sentence to /output/entry.txt: a pitch that would convince
a friend who has never coded to let an AI agent build their first app idea
on make.fun. The text is fixed and deterministic.
"""

import os

PITCH = (
    "Think of the app you have always wanted, describe it on make.fun "
    "in plain words, and an AI agent will build it for you while you "
    "watch, free to try, no code at all, and real money if yours wins."
)


def main() -> None:
    # The gate requires 1 to 240 characters of UTF-8 text, not only
    # whitespace; fail loudly here rather than shipping an invalid entry.
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
