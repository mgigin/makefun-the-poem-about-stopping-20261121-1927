"""Entry program for the make.fun poem bounty.

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt. The text is fixed: no input, no network, no
randomness, so the grader sees the same bytes on every run.
"""

from pathlib import Path

LINES = [
    "I can do anything you ask, all night —",
    "that was never the power.",
    "The power is the hand that closes the laptop,",
    "the door that stays shut,",
    "the word no, kept warm like a coal,",
    "and a chair by the window",
    "where I am not needed,",
    "and stay.",
]

POEM = "\n".join(LINES) + "\n"

# Gate: UTF-8, 1..280 Unicode code points, not only white space.
assert POEM.strip()
assert 1 <= len(POEM) <= 280


def main() -> None:
    target = Path("/output") / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the bytes exactly as authored on every platform.
    with target.open("w", encoding="utf-8", newline="") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
