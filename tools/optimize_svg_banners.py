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

import argparse
import sys

from lxml import etree
from pathlib import Path
from scour import scour

def process() -> None:
    """Processes svg file to minimize size"""
    parser = argparse.ArgumentParser(
        description="Minimize size of svg file.",
    )
    parser.add_argument(
        "filename",
        type=str,
        nargs='+',
        help="Path to svg file, it must end in _source.svg.",
    )
    args = parser.parse_args()
    input_file = args.filename[0]
    if input_file[-11:] != "_source.svg":
         print("Filename should end with '_source.svg'")
         sys.exit(1)

    print("Processing...")
    "with Path(input_file).open("r") as f:"
    "    svg = f.read()"
    tree = etree.parse(input_file)
    print("Removing text fileds")
    targets = tree.xpath('//x:text',namespaces={'x': 'http://www.w3.org/2000/svg'})
    for target in targets:
        target.getparent().remove(target)
    svg = etree.tostring(tree).decode()
    print("Minimizing")
    clean_svg = scour.scourString(svg)
    output_file = input_file.replace("_source.svg",".svg")
    with Path(output_file).open("w", encoding="utf-8") as f:
        f.write(clean_svg)
    print("All done!")


if __name__ == "__main__":
    process()
