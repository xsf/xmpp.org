#!/usr/bin/env python3

"""Tool for maintaining software list entries"""

from typing import Any

import argparse
import copy
import difflib
import json
import sys
from pathlib import Path


def json_as_lines(data: Any) -> list[str]:
    """Returns a json file as newline terminated strings"""
    return [
        line + "\n" for line in json.dumps(data, indent=4, sort_keys=True).split("\n")
    ]


def main() -> None:
    """Main logic of update_entry tool"""
    parser = argparse.ArgumentParser(
        description="Modify a software entry in the software list.",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default=None,
        metavar="NAME",
        help="Current name of the project",
    )

    parser.add_argument(
        "--rename",
        dest="new_name",
        metavar="NAME",
        default=None,
        help="Rename the project",
    )

    parser.add_argument(
        "--set-url",
        dest="new_url",
        metavar="URL",
        default=None,
        help="Change the URL of the project",
    )

    parser.add_argument(
        "--set-doap",
        dest="new_doap",
        metavar="URL",
        default=None,
        help="Change the URL of the project DOAP file",
    )

    parser.add_argument(
        "--set-platforms",
        dest="new_platforms",
        metavar="PLATFORM",
        default=None,
        nargs="+",
        help="Change the contents of the last column",
    )

    parser.add_argument(
        "--no-ask",
        dest="ask",
        default=True,
        action="store_false",
        help="Do not ask for confirmation before applying changes. ",
    )

    args = parser.parse_args()

    with Path("../data/software.json").open(encoding="utf-8") as software_file:
        filename = software_file.name
        data = json.load(software_file)

    name_map = {item["name"]: item for item in data}

    try:
        item = name_map[args.name]
    except KeyError:
        if args.name is not None:
            print(f"Error: no such project: {args.name!r}", file=sys.stderr)
        print("Hint: the following projects exist:")
        print(
            "    ",
            "\n    ".join(sorted(name_map.keys())),
            sep="",
            file=sys.stderr,
        )
        print("Hint: capitalisation matters!", file=sys.stderr)
        sys.exit(1)

    orig = copy.deepcopy(item)

    if args.new_name:
        try:
            existing = name_map[args.new_name]
        except KeyError:
            pass
        else:
            print(
                f"Error: new name {args.new_name!r} already in use by a project",
                file=sys.stderr,
            )
            print("Hint: the existing project looks like this:", file=sys.stderr)
            json.dump(existing, sys.stderr, indent=4, sort_keys=True)
            print(file=sys.stderr)
            sys.exit(2)

        item["name"] = args.new_name

    if args.new_url is not None:
        item["url"] = args.new_url or None

    if args.new_doap is not None:
        item["doap"] = args.new_doap or None

    if args.new_platforms is not None:
        item["platforms"] = list({platform.strip() for platform in args.new_platforms})

    item["platforms"].sort(key=lambda x: x.casefold())

    if args.ask:
        old_entry = json_as_lines(orig)
        new_entry = json_as_lines(item)
        print("difference between old and new:")
        sys.stdout.writelines(
            difflib.unified_diff(
                old_entry,
                new_entry,
                fromfile="before",
                tofile="after",
                n=1000,
            ),
        )

        prompt = "is this okay? [y/n]"
        try:
            chosen = input(prompt)
            while chosen not in "yn":
                print("please choose y or n!")
                chosen = input(prompt)
        except (EOFError, KeyboardInterrupt):
            chosen = "n"

        if chosen != "y":
            print("aborting per user request")
            sys.exit(3)

    data.sort(key=lambda x: x["name"].casefold())

    with Path(filename).open("w", encoding="utf-8") as software_file:
        json.dump(data, software_file, indent=4, sort_keys=True)
        software_file.write("\n")


if __name__ == "__main__":
    main()
