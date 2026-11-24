#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt: a hugging face.
A stranger reading it sees open arms and a warm smile at first
glance, with no words, no irony and nothing to misread.
"""

import os


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write("\U0001f917")


if __name__ == "__main__":
    main()
