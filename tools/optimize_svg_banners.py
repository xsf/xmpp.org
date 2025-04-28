#!/usr/bin/env python3

"""This script minimizes the size of SVG files used as
banners.  This allows for faster loading time in browsers,
but still allows keeping a version of the SVG file that is
suitable for editing and updating as it contains font and
editing layout information.

Based on
https://stackoverflow.com/questions/55812554/try-using-scour-to-clean-an-svg
https://github.com/scour-project/scour/blob/master/scour/scour.py#L3623
"""

from typing import cast

import argparse
import sys
from pathlib import Path

from lxml import etree  # type: ignore  # noqa: PGH003
from scour import scour


def process() -> None:
    """Processes svg file to minimize size"""
    arg_parser = argparse.ArgumentParser(
        description="Minimize size of svg file.",
    )
    arg_parser.add_argument(
        "filename",
        type=str,
        nargs="+",
        help="Path to svg file, it must end in _source.svg.",
    )
    args = arg_parser.parse_args()
    input_file_path = cast("str", args.filename[0])
    if not input_file_path.endswith("_source.svg"):
        print("Filename should end with '_source.svg'")
        sys.exit(1)

    print("Processing...")
    tree = etree.parse(input_file_path)

    print("Removing text fields...")
    targets = tree.xpath("//x:text", namespaces={"x": "http://www.w3.org/2000/svg"})
    for target in targets:
        target.getparent().remove(target)

    svg = etree.tostring(tree).decode()

    print("Minimizing...")
    clean_svg = scour.scourString(svg)
    output_file_path = input_file_path.replace("_source.svg", ".svg")
    with Path(output_file_path).open("w", encoding="utf-8") as f:
        f.write(clean_svg)
    print("All done!")


if __name__ == "__main__":
    process()
