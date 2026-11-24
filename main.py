#!/usr/bin/env python3
"""Entry for u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.

Writes a single-sentence absurd invention pitch to entry.txt.
Gate: UTF-8 text, 1-220 characters, not only whitespace, one sentence.
"""

import os
import stat

ENTRY_TEXT = (
    "A toothpaste tube that squeezes itself from the bottom and files "
    "a formal complaint every time you grab the middle, citing three "
    "years of unreported crimes against dentistry."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
