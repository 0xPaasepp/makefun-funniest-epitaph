#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph -- writes the entry epitaph
(one line, at most 150 characters) to /output/entry.txt.

Pure standard library; deterministic from any working directory.
"""

import os

LINE = "I died as I lived: on hold with customer service."

# Gate: /output/entry.txt must be UTF-8 text of 1-150 characters, one line,
# not only whitespace. Fail loudly instead of writing an invalid entry.
if not (1 <= len(LINE) <= 150) or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-150 char single-line gate")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
