#!/usr/bin/env python3
import argparse
import difflib
import copy
import json
import os.path
import sys

from datetime import datetime

SEPARATOR = ":"


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


def verify_items(items, valid_items):
    if valid_items is None:
        return
    unknown = set(items) - valid_items
    if unknown:
        print(
            "Error: The value(s) {} is/are not defined".format(
                ", ".join(map(repr, unknown))
            ),
            file = sys.stderr,
        )
        print(
            "Hint: The following values are allowed:",
            file = sys.stderr,
        )
        for value in sorted(valid_items, key = sortkey):
            print("   ", value, file = sys.stderr)
        print(
            "Hint: This is ignored by the linting tool for non-renewed",
            "      software, but will be enforced once the software is",
            "      renewed.",
            sep = "\n"
        )
        sys.exit(2)


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
        "--set-platforms",
        dest="new_platforms",
        metavar="PLATFORM",
        default=None,
        nargs="+",
        help="Change the platform list",
    )

    parser.add_argument(
        "--set-features",
        dest="new_features",
        metavar="FEATURE[:COMMENT]",
        default=None,
        nargs="+",
        help="Change the feature list, optionally a comment may be given for each feature",
    )

    parser.add_argument(
        "--no-renewal",
        action="store_false",
        dest="renew",
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

    if "clients" in filename or "servers" in filename:
        with open(os.path.join(
                os.path.dirname(filename),
                "platforms.json")) as f:
            valid_platforms = set(json.load(f))
        with open(os.path.join(
                os.path.dirname(filename),
                "features.json")) as f:
            valid_features = set(feature["id"] for feature in json.load(f))
    else:
        valid_platforms = None
        valid_features = None

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

    if args.new_platforms is not None:
        item["platforms"] = list(set(
            platform.strip()
            for platform in args.new_platforms
        ))
    verify_items(item["platforms"], valid_platforms)
    item["platforms"].sort(key=lambda x: x.casefold())

    if args.new_features is not None:
        item["features"] = list(set(
            feature.strip().split(SEPARATOR)[0]
            for feature in args.new_features
        ))
        item["comments"] = {
            k: v
            for k, v in (
                feature.strip().split(SEPARATOR)
                for feature in args.new_features
                if SEPARATOR in feature
            )
        }
    if item.get("features"):
        verify_items(item["features"], valid_features)
        item["features"].sort(key=lambda x: x.casefold())

    if args.renew:
        item["last_renewed"] = datetime.utcnow().replace(
            microsecond=0
        ).isoformat()

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


if __name__ == "__main__":
    main()
