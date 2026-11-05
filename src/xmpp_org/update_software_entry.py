#!/usr/bin/env python3

"""Tool for maintaining software list entries"""

from typing import Any

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


def update_software_entry(  # noqa: PLR0913, PLR0917
    name: str,
    new_name: str | None = None,
    new_url: str | None = None,
    new_doap: str | None = None,
    new_platforms: str | None = None,
    ask: bool = True,
) -> None:
    """Main logic of update_entry tool"""
    base_path = Path.cwd()
    with Path(base_path / "data" / "software.json").open(
        encoding="utf-8"
    ) as software_file:
        filename = software_file.name
        data = json.load(software_file)

    name_map = {item["name"]: item for item in data}

    try:
        item = name_map[name]
    except KeyError:
        if name is not None:
            print(f"Error: no such project: {name!r}", file=sys.stderr)
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

    if new_name:
        try:
            existing = name_map[new_name]
        except KeyError:
            pass
        else:
            print(
                f"Error: new name {new_name!r} already in use by a project",
                file=sys.stderr,
            )
            print("Hint: the existing project looks like this:", file=sys.stderr)
            json.dump(existing, sys.stderr, indent=4, sort_keys=True)
            print(file=sys.stderr)
            sys.exit(2)

        item["name"] = new_name

    if new_url is not None:
        item["url"] = new_url or None

    if new_doap is not None:
        item["doap"] = new_doap or None

    if new_platforms is not None:
        item["platforms"] = list({platform.strip() for platform in new_platforms})

    item["platforms"].sort(key=lambda x: x.casefold())

    if ask:
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
        except EOFError, KeyboardInterrupt:
            chosen = "n"

        if chosen != "y":
            print("aborting per user request")
            sys.exit(3)

    data.sort(key=lambda x: x["name"].casefold())

    with Path(filename).open("w", encoding="utf-8") as software_file:
        json.dump(data, software_file, indent=4, sort_keys=True)
        software_file.write("\n")
