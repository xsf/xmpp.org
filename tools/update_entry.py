#!/usr/bin/env python3
import argparse
import difflib
import copy
import json
import os.path
import sys

from datetime import datetime


def json_as_lines(data):
    return [
        line+"\n"
        for line in json.dumps(
                data,
                indent=4,
                sort_keys=True
        ).split("\n")
    ]


def sortkey(x):
    return x.casefold()


def main():
    parser = argparse.ArgumentParser(
        description="Modify a software entry in the software list."
    )
    parser.add_argument(
        "listfile",
        type=argparse.FileType("r"),
        metavar="JSONFILE",
        help="Software list JSON file to manipulate",
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
        help="Do not ask for confirmation before applying changes. "
    )

    args = parser.parse_args()

    with args.listfile as f:
        filename = f.name
        data = json.load(f)

    name_map = {item["name"]: item for item in data}

    try:
        item = name_map[args.name]
    except KeyError:
        if args.name is not None:
            print("Error: no such project: {!r}".format(args.name),
                  file=sys.stderr)
        print("Hint: the following projects exist:")
        print(
            "    ", "\n    ".join(sorted(name_map.keys())),
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
                "Error: new name {!r} already in use by a project".format(
                    args.new_name
                ),
                file=sys.stderr,
            )
            print("Hint: the existing project looks like this:",
                  file=sys.stderr)
            json.dump(existing, sys.stderr, indent=4, sort_keys=True)
            print(file=sys.stderr)
            sys.exit(2)

        item["name"] = args.new_name

    if args.new_url is not None:
        item["url"] = args.new_url or None

    if args.new_doap is not None:
        item["doap"] = args.new_doap or None

    if args.new_platforms is not None:
        item["platforms"] = list(set(
            platform.strip()
            for platform in args.new_platforms
        ))

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
            )
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

    with open(filename, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main()
