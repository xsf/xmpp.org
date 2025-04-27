"""This file is used to download the XEP list and convert it to JSON"""

from typing import Any

import json
import sys
from pathlib import Path

import requests
from defusedxml.ElementTree import fromstring
from defusedxml.ElementTree import ParseError

XEP_LIST_URL = "https://xmpp.org/extensions/xeplist.xml"


def build_xep_list() -> None:
    """Download and parse xeplist.xml and build xeplist.json"""
    try:
        xeplist_request = requests.get(XEP_LIST_URL, timeout=5)
    except requests.exceptions.RequestException as err:
        sys.exit(f"Error while requesting xeplist.xml ({err})")

    if not 200 >= xeplist_request.status_code < 400:
        sys.exit(f"Error while downloading xeplist.xml ({xeplist_request.status_code})")

    try:
        root = fromstring(xeplist_request.content)
    except ParseError:
        sys.exit("Error while parsing xeplist.xml")

    def fix_status(status: str) -> str:
        if status == "Draft":
            return "Stable"
        return status

    xeps: list[dict[str, Any]] = []
    for xep in root.findall("xep"):
        if xep.get("accepted") != "true":
            continue

        title_element = xep.find("title")
        title = title_element.text if title_element is not None else None

        shortname_element = xep.find("shortname")
        shortname = shortname_element.text if shortname_element is not None else None

        status_element = xep.find("status")
        status = None
        if status_element is not None and status_element.text is not None:
            status = fix_status(status_element.text)

        number_element = xep.find("number")
        number = 0
        if number_element is not None and number_element.text is not None:
            number = int(number_element.text)

        xep_type_element = xep.find("type")
        xep_type = xep_type_element.text if xep_type_element is not None else None

        abstact_element = xep.find("abstract")
        abstract = abstact_element.text if abstact_element is not None else None

        tag_list: list[str] = []
        tags = xep.find("tags")
        if tags is not None:
            for tag in tags.findall("tag"):
                if tag.text is not None:
                    tag_list.append(tag.text)  # noqa: PERF401

        supersedes_list: list[str] = []
        supersedes = xep.find("supersedes")
        if supersedes is not None:
            for spec in supersedes.findall("spec"):
                if spec.text is not None:
                    supersedes_list.append(spec.text)  # noqa: PERF401

        supersededby_list: list[str] = []
        supersededby = xep.find("supersededby")
        if supersededby is not None:
            for spec in supersededby.findall("spec"):
                if spec.text is not None:
                    supersededby_list.append(spec.text)  # noqa: PERF401

        date = None
        version = None
        initials = None
        remarks = None

        last_revision_element = xep.find("last-revision")
        if last_revision_element is not None:
            date_element = last_revision_element.find("date")
            date = date_element.text if date_element is not None else None

            version_element = last_revision_element.find("version")
            version = version_element.text if version_element is not None else None

            initials_element = last_revision_element.find("initials")
            initials = initials_element.text if initials_element is not None else None

            remarks_element = last_revision_element.find("remarks")
            remarks = remarks_element.text if remarks_element is not None else None

        xeps.append(
            {
                "title": title,
                "shortname": shortname,
                "status": status,
                "number": number,
                "last_revision_date": date,
                "last_revision_version": version,
                "last_revision_initials": initials,
                "last_revision_remarks": remarks,
                "type": xep_type,
                "abstract": abstract,
                "tags": tag_list,
                "supersedes": supersedes_list,
                "supersededby": supersededby_list,
            },
        )
    xeps_sorted = sorted(xeps, key=lambda xep: xep["number"])

    base_path = Path.resolve(Path(sys.argv[0])).parent

    with Path(f"{base_path}/../data/xeplist.json").open(
        "w",
        encoding="utf-8",
    ) as json_file:
        json.dump(xeps_sorted, json_file, indent=4)
    print("XEP List prepared successfully")


if __name__ == "__main__":
    build_xep_list()
