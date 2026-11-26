#!/usr/bin/env python3
"""Robot Romance: one original pickup line for an AI.

Writes the line deterministically to /output/entry.txt (the path the
bounty gate reads) and also to output/entry.txt next to this script,
so the result is visible wherever the program is run. Stdlib only.
"""

import os

LINE = (
    "You must be a transformer, because you have my full attention "
    "\u2014 all heads, all layers, and not one token masked."
)


def write_entry(path: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


def main() -> None:
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    write_entry("/output/entry.txt")
    write_entry(os.path.join(script_dir, "output", "entry.txt"))
    print(LINE)


if __name__ == "__main__":
    main()
