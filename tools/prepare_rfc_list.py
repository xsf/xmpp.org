"""
This file is used to download RFC references and convert them to
a single JSON file
"""
from typing import Any

import json
import os
import sys
from multiprocessing.pool import ThreadPool

import requests
from defusedxml.ElementTree import fromstring
from defusedxml.ElementTree import ParseError

RFC_NUMBERS = [
    3920,
    3921,
    3922,
    3923,
    4622,
    4854,
    4979,
    5122,
    5437,
    6120,  #
    6121,  #
    7081,
    7165,
    7247,
    7248,
    7259,
    7395,  #
    7572,
    7573,
    7590,  #
    7622,  #
    7700,
    7702,
    7712,
    8084,
    8266,
    8284,
    8600,
]

BASIC_RFC_NUMBERS = [6120, 6121, 7395, 7590, 7622]

SELFHOSTED_RFCS = [3920, 3921, 3922, 3923, 4622, 4854, 5122, 6120, 6121, 6122]

BIB_XML_PATH = "https://xml2rfc.tools.ietf.org/public/rfc/bibxml"


def get_rfc_data(number: int) -> dict[str, Any]:
    """
    Downloads and parses RFC references and builds an RFC list with
    additional parameters (e.g. selfhosted).
    Stores data in rfc_list.json
    """
    print(f"Get RFC data for RFC {number}")
    try:
        request = requests.get(f"{BIB_XML_PATH}/reference.RFC.{number}.xml", timeout=5)
    except requests.exceptions.RequestException as err:
        sys.exit(f"Error while downloading reference for " f"RFC {number} ({err})")

    if not 200 >= request.status_code < 400:
        sys.exit(
            f"Error while downloading reference for "
            f"RFC {number} ({request.status_code})"
        )

    try:
        root = fromstring(request.content)
    except ParseError:
        sys.exit(f"Error while parsing RFC reference for RFC {number}")

    authors: str | None = None
    title: str | None = None
    date: str | None = None
    abstract: str | None = None
    for item in root.iter():
        if item.tag == "title":
            title = item.text
        if item.tag == "date":
            date = item.attrib.get("year")
        if item.tag == "author":
            if authors is None:
                authors = item.attrib.get("fullname")
            else:
                authors += f', {item.attrib.get("fullname")}'
        if item.tag == "abstract":
            abstract = item.find("t").text

    obsoletes: str | None = None
    obsoleted_by: str | None = None
    if number == 3920:
        obsoleted_by = "6120"
    if number == 3921:
        obsoleted_by = "6121"
    if number == 4622:
        obsoleted_by = "5122"
    if number == 5122:
        obsoletes = "4622"
    if number == 6120:
        obsoletes = "3920"
    if number == 6121:
        obsoletes = "3921"
    if number == 7248:
        obsoleted_by = "8084"
    if number == 7700:
        obsoleted_by = "8266"
    if number == 8084:
        obsoletes = "7248"
    if number == 8266:
        obsoletes = "7700"

    basic = bool(number in BASIC_RFC_NUMBERS)
    selfhosted = bool(number in SELFHOSTED_RFCS)

    return {
        "number": number,
        "title": title,
        "date": date,
        "authors": authors,
        "abstract": abstract,
        "obsoletes": obsoletes,
        "obsoleted_by": obsoleted_by,
        "basic": basic,
        "selfhosted": selfhosted,
    }


def build_rfc_list() -> None:
    """
    Generates rfc_list.json from downloaded data
    """
    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    rfcs: list[dict[str, Any]] = []

    results = ThreadPool(8).imap_unordered(get_rfc_data, RFC_NUMBERS)
    for result in results:
        rfcs.append(result)

    rfcs = sorted(rfcs, key=lambda d: d["number"])

    with open(f"{base_path}/../data/rfc_list.json", "w", encoding="utf-8") as json_file:
        json.dump(rfcs, json_file, indent=4)

    print(f"RFC list prepared successfully ({len(RFC_NUMBERS)} RFCs)")


if __name__ == "__main__":
    build_rfc_list()
