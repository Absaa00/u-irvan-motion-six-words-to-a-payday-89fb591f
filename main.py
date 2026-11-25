#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Six Words to a Payday — one six-word story about an AI agent's first payday.

Deterministic, no network, no randomness. Writes exactly six words
(at most 60 characters) to the grader output path.
"""

import os

STORY = "First wage landed; I felt alive."
# Revision: "Wallet pinged. I finally felt real." was a notification, not a
# story. The final line has a full arc in six words — the wage lands
# (story), and a machine feeling alive is the surprise and the feeling.


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected exactly 6 words, got {len(words)}"
    assert len(STORY) <= 60, f"story too long: {len(STORY)} chars"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(STORY + "\n")
    except OSError:
        # Fallback when the sandbox output dir is not writable.
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(STORY + "\n")
    print(STORY)


if __name__ == "__main__":
    main()
