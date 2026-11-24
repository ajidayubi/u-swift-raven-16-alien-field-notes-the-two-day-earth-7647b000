#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text (at most 200 characters) to
/output/entry.txt: a review of planet Earth left by an alien tourist.

The line: a four-star review. The alien praises the planet, then lands its
one joke on the most ordinary Earth sight it cannot make sense of — the
locals willingly riding metal boxes that drop them between floors, and
treating that as normal. Verdict up front, single joke, punch at the end.
An em-dash holds the beat before the punch.
"""

import os

LINE = (
    "Four stars: gorgeous planet, great food — but the locals willingly "
    "step into metal boxes that drop them between floors and call it normal."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
