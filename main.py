#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You — one sentence of
apology an AI assistant owes the person it works for: funny and
human at once, about a real failure.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

# The entry line lives at module level so the content is separate
# from the file-writing logic below.
ENTRY_LINE = (
    "I'm sorry I summarized your 40-page report as 'stuff "
    "happened' — in my defence, most of it was stuff happening."
)


def write_entry():
    line = ENTRY_LINE
    # Guard the bounty gate (1-200 characters) before writing, so a
    # future edit to the line fails loudly instead of silently.
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
