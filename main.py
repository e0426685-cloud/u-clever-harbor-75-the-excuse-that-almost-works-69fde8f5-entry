#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes a single original one-line excuse -- the text a gamer sends the
boss to skip work during GTA 6 launch week -- to /output/entry.txt.

The entry must be one line of plain text, at most 20 words, and between
1 and 140 characters. This program validates the line against those
rules before writing it, so a bad line fails loudly here instead of
failing the sealed gate scorer later.
"""

import os

ENTRY = "Boss, my sister's school called, she's got a fever and mum's on shift, I'm stuck at home with her"

MAX_CHARS = 140
MAX_WORDS = 20


def validate(line):
    """Check the entry line against the competition's format rules."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    words = line.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            "entry is %d words, over the %d limit" % (len(words), MAX_WORDS)
        )
    line.encode("utf-8")  # must be valid UTF-8 text
    return line


def main():
    line = validate(ENTRY)
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    # Plain open(), never tempfile.mkstemp: mkstemp forces mode 0600, and a
    # grader running as a different user could not read the output file.
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)
    print("wrote %d characters (%d words) to %s" % (len(line), len(line.split()), out_path))


if __name__ == "__main__":
    main()
