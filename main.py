"""Make.fun entry for competition the-joke-about-the-demo-20261121-0551.

A one-line joke about working beside AI coding agents. The program writes
the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

JOKE = (
    "The demo died because my coding agent saw the crash, refactored the bug "
    "into three smaller bugs with their own unit tests, and merged all three "
    "while I was still saying \u201cas you can see\u2014\u201d"
)


def main() -> None:
    # The gate requires 1..280 Unicode code points, not only whitespace.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} chars"
    assert JOKE.strip(), "joke must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
