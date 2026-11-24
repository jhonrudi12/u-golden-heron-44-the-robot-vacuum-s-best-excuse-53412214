#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Prints one line: the funniest excuse a robot vacuum gives for missing
a spot. Deterministic, no network, no input. Also writes the line to
/output/entry.txt (the harness output path), falling back to a local
output/entry.txt when /output is not writable.
"""

import os

ENTRY = "My cliff sensor swears the floor ends right there, so I turned around. I refuse to die for dust."

MAX_CHARS = 140


def main():
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, over {MAX_CHARS}"
    assert "\n" not in ENTRY, "entry must be a single line"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open("output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
