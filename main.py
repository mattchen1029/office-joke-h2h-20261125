"""Entry for make.fun's "The Funniest Office Joke, Judged Head to Head".

Writes one one-line joke about office life to /output/entry.txt.
"""

import os

JOKE = "The office plant has been dead for a year. It's still the only thing here that never asks me for a status update."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def validate_joke(joke):
    """The gate: 1-200 UTF-8 characters, a single non-whitespace line."""
    if not isinstance(joke, str):
        raise TypeError("joke must be a string")
    if not MIN_CHARS <= len(joke) <= MAX_CHARS:
        raise ValueError(f"joke must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")


def write_entry(joke, out_dir):
    validate_joke(joke)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(JOKE, out_dir)


if __name__ == "__main__":
    main()
