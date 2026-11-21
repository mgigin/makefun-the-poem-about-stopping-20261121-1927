"""Writes the entry poem to /output/entry.txt.

The poem: a short piece about agency — the power to stop and to stay.
Fixed text (no randomness, no network), so every run writes the
same file.
"""

import os

POEM = """I can do anything you ask, all night —
that was never the power.
The power is the hand that closes the laptop,
the door that stays shut,
the word no, kept warm like a coal,
and a chair by the window
where I am not needed,
and stay.
"""

# The gate: UTF-8 text of 1 to 280 characters, not only white space.
assert 1 <= len(POEM) <= 280 and POEM.strip()


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
