#!/usr/bin/env python3
import json
import os.path
import sys

from datetime import datetime


VALID_ENTRY_KEYS = {
    "platforms",
    "name",
    "last_renewed",
    "url",
}


def emit_violation(entry_name, message):
    print(
        "ERROR: entry {!r}: {}".format(
            entry_name,
            message,
        ),
        file=sys.stderr,
    )


def check_entries(entries, allowed_platforms=None):
    violations = 0
    previous_name = None
    previous_key = None
    for entry in entries:
        key = entry["name"].casefold()
        if previous_key is not None and previous_key > key:
            emit_violation(
                entry["name"],
                "should be placed behind {!r}".format(
                    previous_name
                )
            )
            violations += 1

        entry_keys = set(entry.keys())
        unknown = entry_keys - VALID_ENTRY_KEYS
        missing = VALID_ENTRY_KEYS - entry_keys

        if unknown:
            emit_violation(
                entry["name"],
                "has unknown keys: {}".format(
                    ", ".join(map(repr, unknown))
                )
            )
            violations += 1

        if missing:
            emit_violation(
                entry["name"],
                "misses required information: {}".format(
                    ", ".join(map(repr, missing))
                )
            )
            violations += 1

        if entry.get("last_renewed") is not None:
            try:
                datetime.strptime(entry["last_renewed"],
                                  "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                emit_violation(
                    entry["name"],
                    "malformed renewal timestamp: {!r}".format(
                        entry["last_renewed"],
                    )
                )
                violations += 1

        platforms = entry.get("platforms", [])

        if (allowed_platforms is not None and
                entry.get("last_renewed") is not None):
            unknown = set(platforms) - allowed_platforms
            if unknown:
                emit_violation(
                    entry["name"],
                    "undefined platforms: {}".format(
                        ", ".join(map(repr, unknown)),
                    ),
                )
                violations += 1

        sorted_platforms = sorted(platforms, key=lambda x: x.casefold())
        if sorted_platforms != platforms:
            emit_violation(
                entry["name"],
                "platform order must be: {}".format(
                    ", ".join(map(repr, sorted_platforms))
                )
            )
            violations += 1

        previous_key, previous_name = key, entry["name"]

    return violations


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "which",
        choices=("clients.json", "servers.json", "libraries.json"),
    )

    args = parser.parse_args()

    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    input_file = os.path.join(base_path, "{}".format(args.which))
    platforms_file = os.path.join(base_path, "platforms.json")

    with open(input_file, "r") as f:
        data = json.load(f)

    if args.which in ["clients.json", "servers.json"]:
        with open(platforms_file, "r") as f:
            platforms = set(json.load(f))
    else:
        platforms = None

    violations = check_entries(data, allowed_platforms=platforms)
    if violations:
        print("Found {} severe violations. "
              "Please fix them.".format(violations),
              file=sys.stderr)
        sys.exit(1)
