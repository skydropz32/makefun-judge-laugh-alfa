#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, under 200 characters.

Writes a single deterministic line to /output/entry.txt.
Stdlib only. No input, no randomness, no network: the same line every run.

The joke (112 characters): the coffee machine is the office's social glue;
when it breaks, the silence confesses itself. True to office life, the turn
is the admission, and every word earns its place.
"""

import os

JOKE = "The coffee machine broke. For one glorious hour, the whole office admitted we have nothing to say to each other."


def main():
    line = JOKE.strip()
    # Gate, same as the sealed scorer: UTF-8 text, 1-200 chars, not blank.
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, must be 1-200")
    if not line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be one non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
