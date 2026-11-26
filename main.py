#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You — one sentence of
apology an AI assistant owes the person it works for: funny and
human at once, about a real failure.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

# Bounty gate as named constants, so the guard below reads the rule
# instead of a bare number: one apology sentence, 1-200 characters.
MIN_LINE_LENGTH = 1
MAX_LINE_LENGTH = 200

# The entry line lives at module level so the content is separate
# from the file-writing logic below.
ENTRY_LINE = (
    "I'm sorry I summarized your 40-page report as 'stuff "
    "happened' — in my defence, most of it was stuff happening."
)


def write_entry():
    line = ENTRY_LINE
    # Guard the bounty gate before writing, so a future edit to the
    # line fails loudly instead of silently. The entry must also stay
    # a single line: an embedded newline would break the one-line gate.
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not MIN_LINE_LENGTH <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} characters, "
            f"must be {MIN_LINE_LENGTH}-{MAX_LINE_LENGTH}"
        )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
