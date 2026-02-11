#!/usr/bin/env python3
"""Lint software.json"""

from typing import Any

import json
import sys
from pathlib import Path

VALID_ENTRY_KEYS = {
    "platforms",
    "name",
    "doap",
    "url",
    "categories",
}


def emit_violation(entry_name: str, message: str, warning: bool = False) -> None:
    """Prints warnings and errors"""
    prefix = "WARN" if warning else "ERROR"
    print(f"{prefix}: entry {entry_name!r}: {message}")


def check_entries(entries: list[dict[str, Any]]) -> int:
    """Checks entries for violations and returns their count"""
    violations = 0
    previous_name = None
    previous_key = None
    for entry in entries:
        key = entry["name"].casefold()
        if previous_key is not None and previous_key > key:
            emit_violation(
                entry["name"],
                f"should be placed in front of {previous_name!r} (all entries must be "
                f"ordered alphabetically by case-folded name)",
            )
            violations += 1

        entry_keys = set(entry.keys())
        unknown = entry_keys - VALID_ENTRY_KEYS
        missing = VALID_ENTRY_KEYS - entry_keys

        if unknown:
            emit_violation(
                entry["name"],
                f"has unknown keys: {', '.join(map(repr, unknown))}",
            )
            violations += 1

        if missing:
            emit_violation(
                entry["name"],
                f"misses the following required properties: "
                f"{', '.join(map(repr, missing))} "
                f"(see other entries for a reference)",
            )
            violations += 1

        supported_platforms = entry.get("platforms", [])

        sorted_platforms = sorted(supported_platforms, key=lambda x: x.casefold())
        if sorted_platforms != supported_platforms:
            emit_violation(
                entry["name"],
                f"platform order must be: "
                f"{', '.join(map(repr, sorted_platforms))} "
                f"(platforms must be ordered alphabetically)",
            )
            violations += 1

        doap = entry.get("doap")
        url = entry.get("url")
        if doap is not None and (url is not None or supported_platforms):
            emit_violation(
                entry["name"],
                "a DOAP file is linked, therefore 'url' must be null and "
                "'platforms' must be [], because the DOAP file provides both",
            )
            violations += 1

        previous_key, previous_name = key, entry["name"]

    return violations


if __name__ == "__main__":
    file_name = Path(sys.argv[1]).name
    base_path = Path.resolve(Path(__file__)).parent.parent
    input_file = Path(base_path / "data" / file_name)
    with Path(input_file).open("rb") as data_file:
        data = json.load(data_file)

    violations_count = check_entries(data)
    if violations_count:
        print(
            f"Found {violations_count} severe violations in {file_name}."
            "Please fix them.",
        )
        sys.exit(1)

    print(f"Lint check passed successfully for {file_name}")
