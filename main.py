#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt: a hugging face.
A stranger reading it sees open arms and a warm smile at first
glance, with no words, no irony and nothing to misread.
"""

import os

# U+1F917 HUGGING FACE: open arms and a warm smile at first glance,
# kind and friendly with no context needed, and a deliberate pick
# rather than the first smiley that comes to mind.
EMOJI = "\U0001f917"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
