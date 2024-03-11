"""
This file is used to download the XEP list and convert it to JSON
"""
from typing import Any

import json
import os
import sys

import requests
from defusedxml.ElementTree import fromstring
from defusedxml.ElementTree import ParseError

XEP_LIST_URL = "https://xmpp.org/extensions/xeplist.xml"


def build_xep_list() -> None:
    """
    Download and parse xeplist.xml and build xeplist.json
    """
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
        if xep.get("accepted") == "true":
            shortname = xep.find("shortname")
            if shortname is not None:
                shortname = shortname.text

            tag_list: list[str] = []
            tags = xep.find("tags")
            if tags is not None:
                for tag in tags.findall("tag"):
                    tag_list.append(tag.text)

            date_element = xep.find("last-revision").find("date")
            date = date_element.text if date_element is not None else None

            version_element = xep.find("last-revision").find("version")
            version = version_element.text if version_element is not None else None

            initials_element = xep.find("last-revision").find("initials")
            initials = initials_element.text if initials_element is not None else None

            remarks_element = xep.find("last-revision").find("remarks")
            remarks = remarks_element.text if remarks_element is not None else None


            xeps.append(
                {
                    "title": xep.find("title").text,
                    "shortname": shortname,
                    "status": fix_status(xep.find("status").text),
                    "number": int(xep.find("number").text),
                    "last_revision_date": date,
                    "last_revision_version": version,
                    "last_revision_initials": initials,
                    "last_revision_remarks": remarks,
                    "type": xep.find("type").text,
                    "abstract": xep.find("abstract").text,
                    "tags": tag_list,
                }
            )
    xeps_sorted = sorted(xeps, key=lambda xep: xep["number"])

    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    with open(f"{base_path}/../data/xeplist.json", "w", encoding="utf-8") as json_file:
        json.dump(xeps_sorted, json_file, indent=4)
    print("XEP List prepared successfully")


if __name__ == "__main__":
    build_xep_list()
