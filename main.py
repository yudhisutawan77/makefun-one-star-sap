#!/usr/bin/env python3
"""One Star, Written in Sap -- make.fun entry.

Writes a single one-line, one-star review in the voice of a houseplant
about its human owner. The text goes to stdout and to $ENTRY_OUT, which
the harness may pass as a file path or as a directory (in which case the
entry is written to entry.txt inside it).
"""

import os
import sys

REVIEW = (
    "One star. He named me Kevin, repotted me mid-winter, then apologised "
    "to the DOG for the mess. I am writing this review in my own sap. "
    "Do not buy this human."
)


def resolve_output_path():
    """Return the file path the entry text goes to."""
    entry_out = os.environ.get("ENTRY_OUT", "").strip()
    if not entry_out:
        return os.path.join("output", "entry.txt")
    if os.path.isdir(entry_out) or entry_out.endswith(os.sep):
        return os.path.join(entry_out, "entry.txt")
    return entry_out


def main():
    text = REVIEW.strip()
    # The sealed gate only accepts UTF-8 text of 1 to 279 characters, so
    # fail loudly here instead of shipping an entry the judge never sees.
    if not 1 <= len(text) <= 279:
        raise SystemExit(
            "entry is %d characters, gate needs 1-279" % len(text)
        )
    sys.stdout.write(text + "\n")
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
