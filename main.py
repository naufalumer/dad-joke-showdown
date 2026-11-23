"""Dad Joke Showdown entry.

Writes one dad joke, exactly as written below, to entry.txt in the
output directory the grader provides. No network, no third-party
imports, no randomness: the same bytes come out on every run.
"""

import os

JOKE = "I told my kids the fog never stays for dinner. It just mists the moment, then it's gone."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    if not text.strip():
        raise SystemExit("joke must not be blank")
    if not 1 <= len(text) <= 200:
        raise SystemExit("joke must be 1 to 200 characters, got %d" % len(text))
    text.encode("utf-8")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise SystemExit("entry.txt did not round-trip byte-identical")


if __name__ == "__main__":
    main()
