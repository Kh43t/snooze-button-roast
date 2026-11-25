"""Snooze Button Roast -- make.fun entry.

Writes a single-line roast of an alarm clock that rings at 6 AM on a
Saturday to /output/entry.txt. The roast is fixed text: the judge
compares lines head to head, so the program's job is to deliver the
line exactly -- UTF-8, one line, 1-200 characters, readable by
everyone (mode 0644).
"""

import os
import sys

ROAST = "My alarm clock rings at 6 AM on Saturday like the weekend is a rumor it refuses to believe."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def check_roast(text: str) -> None:
    """Refuse anything the gate would refuse, before writing it."""
    if not text or not text.strip():
        raise ValueError("roast is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast is {len(text)} characters, gate allows 1-200")


def main() -> int:
    os.umask(0o022)
    check_roast(ROAST)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)
    try:
        os.chmod(OUTPUT_PATH, 0o644)
        os.chmod(OUTPUT_DIR, 0o755)
    except OSError:
        pass
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ROAST:
        raise ValueError("entry.txt does not match the roast")
    if written.endswith("\n") or "\n" in written:
        raise ValueError("entry.txt must hold exactly one line, no newline")
    print(f"wrote {len(ROAST)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
