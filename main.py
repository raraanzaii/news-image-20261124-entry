#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261124.

The entry image (entry.png, a one-page newspaper front sheet summing up
the world news of Tuesday 24 November 2026) is committed in this
repository next to this program. The grader runs this program offline,
twice, and both runs must write identical bytes to the output file, so
the program simply copies the committed image byte for byte.

Standard library only. The output directory is /output, or the
MAKEFUN_OUTPUT_DIR environment variable when it is set.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(here, IMAGE_NAME)
    if os.path.isfile(candidate):
        return candidate
    # The grader mounts the repository at /bot.
    return os.path.join("/bot", IMAGE_NAME)


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, IMAGE_NAME)


def main():
    src = source_path()
    dst = output_path()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    # Sanity check: the copy must be exactly as large as the source, so a
    # truncated write can never slip through as a valid run.
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        raise IOError("copy size mismatch: %d != %d" % (src_size, dst_size))
    print("wrote %s (%d bytes)" % (dst, dst_size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
