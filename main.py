#!/usr/bin/env python3
"""Entry for make.fun's "The Funniest Office Joke, Judged Head to Head".

Writes one original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only, no network.
"""

import os

JOKE = (
    "The office printer only ever jams on urgent documents \u2014 "
    "it's the only one in this building who actually reads the deadlines."
)


def main() -> None:
    # The gate needs 1-200 characters of real text; fail loudly, never
    # silently ship an entry the gate would refuse.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke outside the 1-200 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
