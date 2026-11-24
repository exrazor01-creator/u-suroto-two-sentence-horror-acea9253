#!/usr/bin/env python3
"""Two-Sentence Horror - make.fun bounty u-suroto-two-sentence-horror-acea9253.

Pure stdlib. Writes the entry text to /output/entry.txt and prints it.
The story must be exactly two sentences, 1..400 characters.
"""

import os

STORY = (
    "Every night, my daughter knocks three times on my bedroom door "
    "before coming in, so I always know it is her. "
    "Tonight the knocking stopped at two, and a small voice whispered "
    "through the wood that it had forgotten the number."
)


def count_sentence_enders(text):
    """Count sentence-ending periods, ignoring abbreviations.

    The story uses no abbreviations and no '!' or '?', so every '.'
    is a sentence ender. Exactly two are required.
    """
    return text.count(".")


def main():
    text = STORY.strip()
    assert 1 <= len(text) <= 400, f"length {len(text)} out of range"
    assert "!" not in text and "?" not in text, "no ! or ? allowed"
    assert count_sentence_enders(text) == 2, (
        f"expected exactly 2 sentences, found {count_sentence_enders(text)} enders"
    )
    assert text.endswith("."), "story must end with a period"
    assert text == text.strip() and "  " not in text, "no stray whitespace"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

    print(text)
    print(f"[{len(text)} characters, {count_sentence_enders(text)} sentences]")


if __name__ == "__main__":
    main()
