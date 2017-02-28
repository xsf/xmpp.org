#!/usr/bin/env python3
import argparse
import copy
import json
import sys

from datetime import datetime


def main():
    parser = argparse.ArgumentParser(
        description="Renew a software entry in the software list."
    )
    parser.add_argument(
        "listfile",
        type=argparse.FileType("r"),
        metavar="JSONFILE",
        help="Software list JSON file to manipulate",
    )
    parser.add_argument(
        "name",
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
        "--set-info",
        dest="new_info",
        metavar="INFO",
        default=None,
        nargs="+",
        help="Change the contents of the last column",
    )

    parser.add_argument(
        "--no-renewal",
        action="store_false",
        dest="renew",
    )

    parser.add_argument(
        "--ask",
        dest="ask",
        action="store_true",
        help="Ask for confirmation before applying changes. "
        "Set this to true if you are unsure on how to use this tool."
    )

    args = parser.parse_args()

    with args.listfile as f:
        filename = f.name
        data = json.load(f)

    name_map = {item["name"]: item for item in data}

    try:
        item = name_map[args.name]
    except KeyError:
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

    if args.new_info is not None:
        item["info"] = [info_item.strip()
                        for info_item in args.new_info]

    if args.renew:
        item["last_renewed"] = datetime.utcnow().replace(
            microsecond=0
        ).isoformat()

    if args.ask:
        print("old entry:")
        json.dump(orig, sys.stdout, indent=4, sort_keys=True)
        print()
        print()
        print("new entry:")
        json.dump(item, sys.stdout, indent=4, sort_keys=True)
        print()
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

    with open(filename, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
