#!/usr/bin/env python3
import json
import os.path
import sys

from datetime import datetime, timedelta


VALID_ENTRY_KEYS = {
    "platforms",
    "name",
    "last_renewed",
    "url",
}


def emit_violation(entry_name, message, *, warning=False):
    prefix = "WARN" if warning else "ERROR"
    print(
        "{}: entry {!r}: {}".format(
            prefix,
            entry_name,
            message,
        ),
        file=sys.stderr,
    )


def check_entries(entries,
                  allowed_platforms=None,
                  show_warnings=False):
    violations = 0
    previous_name = None
    previous_key = None
    for entry in entries:
        key = entry["name"].casefold()
        if previous_key is not None and previous_key > key:
            emit_violation(
                entry["name"],
                "should be placed behind {!r} (all entries must be "
                "ordered alphabetically by case-folded name)".format(
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
                "misses the following required properties: {} "
                "(see other entries for a reference)".format(
                    ", ".join(map(repr, missing))
                )
            )
            violations += 1

        if entry.get("last_renewed") is not None:
            try:
                dt = datetime.strptime(entry["last_renewed"],
                                       "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                emit_violation(
                    entry["name"],
                    "malformed renewal timestamp: {!r} "
                    "(format is YYYY-MM-DDThh:mm:ss)".format(
                        entry["last_renewed"],
                    )
                )
                violations += 1
            else:
                now = datetime.utcnow()
                # some slack, we don’t know how accurate travis
                # clock is and also timezone stuff
                if dt - now > timedelta(hours=24):
                    emit_violation(
                        entry["name"],
                        "renewal date must not be in the future",
                    )
                    violations += 1

        platforms = entry.get("platforms", [])

        if allowed_platforms is not None:
            is_severe = entry.get("last_renewed") is not None
            unknown = set(platforms) - allowed_platforms
            if unknown and (is_severe or show_warnings):
                emit_violation(
                    entry["name"],
                    "undefined platforms: {} "
                    "(the allowed platforms are listed in platforms.json. If"
                    " you think a platform is missing add it and mention it "
                    "in your Pull Request)".format(
                        ", ".join(map(repr, unknown)),
                    ),
                    warning=not is_severe
                )
                violations += is_severe

        sorted_platforms = sorted(platforms, key=lambda x: x.casefold())
        if sorted_platforms != platforms:
            emit_violation(
                entry["name"],
                "platform order must be: {} "
                "(platforms must be ordered alphabetically)".format(
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
    parser.add_argument(
        "-W",
        default=False,
        dest="warnings",
        action="store_true",
        help="Show warnings in addition to errors",
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

    violations = check_entries(
        data,
        allowed_platforms=platforms,
        show_warnings=args.warnings,
    )
    if violations:
        print("Found {} severe violations. "
              "Please fix them.".format(violations),
              file=sys.stderr)
        sys.exit(1)
