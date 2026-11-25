"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to entry.txt inside the
output directory. Stdlib only, deterministic: the same line on every run.

The roast aims at the fridge's firmware and its ice maker: the machine
refuses to make ice until its owner installs a firmware update and accepts
the terms, so the cubes are held hostage by a EULA.
"""

import os

LINE = (
    "My smart fridge won't make ice until I install its firmware update "
    "and accept the terms \u2014 my cubes are held hostage by a EULA."
)


def output_dir():
    """Honour the harness output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text):
    """Gate check, mirroring the sealed scorer: UTF-8, 1-200 chars, not blank."""
    if not text or text != text.strip():
        raise SystemExit("roast line must not be blank or padded")
    if not 1 <= len(text) <= 200:
        raise SystemExit("roast line must be 1-200 characters")
    text.encode("utf-8")
    return text


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    text = validate(LINE.strip())
    path = os.path.join(out_dir, "entry.txt")
    payload = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    os.chmod(path, 0o644)
    # Read back what the grader will see and confirm it is exactly the line.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != payload:
        raise SystemExit("entry.txt read-back does not match the roast line")
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
