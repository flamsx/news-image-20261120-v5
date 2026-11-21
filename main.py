#!/usr/bin/env python3
"""Entry point for news-image-20261120 v5.

Stdlib only. Copies the pre-rendered front page (entry.png, 1024x1024,
under 1 MiB) to /output/entry.png after verifying its PNG magic, its
IHDR dimensions and its sha256. The image itself was drawn locally by
draw.py (Pillow + Lexend); this program does no drawing and needs no
third-party library, so it runs in the grading sandbox as-is.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
EXPECTED_SHA256 = "93130a627f5ec5d15101c501bdbae218ccb427ba91df4093d6c6eb167ea37740"
MAX_BYTES = 1048576


def main():
    with open(SRC, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png over 1 MiB: %d bytes" % len(data))
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.png sha256 mismatch")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1024, 1024):
        raise SystemExit("entry.png is %dx%d, expected 1024x1024" % (width, height))
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")
    print("wrote /output/entry.png (%d bytes, 1024x1024)" % len(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
