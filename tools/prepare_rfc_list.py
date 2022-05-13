'''
This file is used to download RFC references and convert them to
a single JSON file
'''
from typing import Any
from typing import Optional

import sys
import os
import json

from defusedxml.ElementTree import fromstring
from defusedxml.ElementTree import ParseError
import requests

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
    8600
]

BASIC_RFC_NUMBERS = [
    6120,
    6121,
    7395,
    7590,
    7622
]

SELFHOSTED_RFCS = [
    3920,
    3921,
    3922,
    3923,
    4622,
    4854,
    5122,
    6120,
    6121,
    6122
]

BIB_XML_PATH = 'https://xml2rfc.tools.ietf.org/public/rfc/bibxml'


def status_ok(status_code: int) -> bool:
    '''
    Status codes ranging from 200 (OK) to 300 (redirects) are okay
    '''
    if not 200 >= status_code < 400:
        return False
    return True


def build_rfc_list() -> None:
    '''
    Downloads and parses RFC references and builds an RFC list with
    additional parameters (e.g. selfhosted).
    Stores data in rfc_list.json
    '''
    rfcs: list[dict[str, Any]] = []

    for number in RFC_NUMBERS:
        request = requests.get(f'{BIB_XML_PATH}/reference.RFC.{number}.xml')
        if not status_ok(request.status_code):
            sys.exit(f'Error while downloading reference for '
                    f'RFC {number} ({request.status_code})')

        try:
            root = fromstring(request.content)
        except ParseError:
            sys.exit(f'Error while parsing RFC reference for RFC {number}')

        authors: Optional[str] = None
        title: Optional[str] = None
        date: Optional[str] = None
        abstract: Optional[str] = None
        for item in root.iter():
            if item.tag == 'title':
                title = item.text
            if item.tag == 'date':
                date = item.attrib.get('year')
            if item.tag == 'author':
                if authors is None:
                    authors = item.attrib.get('fullname')
                else:
                    authors += f", {item.attrib.get('fullname')}"
            if item.tag == 'abstract':
                abstract = item.find('t').text

        obsoletes: Optional[str] = None
        obsoleted_by: Optional[str] = None
        if number == 3920:
            obsoleted_by = '6120'
        if number == 3921:
            obsoleted_by = '6121'
        if number == 4622:
            obsoleted_by = '5122'
        if number == 5122:
            obsoletes = '4622'
        if number == 6120:
            obsoletes = '3920'
        if number == 6121:
            obsoletes = '3921'
        if number == 7248:
            obsoleted_by = '8084'
        if number == 7700:
            obsoleted_by = '8266'
        if number == 8084:
            obsoletes = '7248'
        if number == 8266:
            obsoletes = '7700'

        basic = bool(number in BASIC_RFC_NUMBERS)
        selfhosted = bool(number in SELFHOSTED_RFCS)

        rfcs.append(
            {
                'number': number,
                'title': title,
                'date': date,
                'authors': authors,
                'abstract': abstract,
                'obsoletes': obsoletes,
                'obsoleted_by': obsoleted_by,
                'basic': basic,
                'selfhosted': selfhosted,
            }
        )
        print('Added RFC', number)

    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    with open(f'{base_path}/../data/rfc_list.json',
              'w',
              encoding='utf-8') as json_file:
        json.dump(rfcs, json_file, indent=4)

    print(f'RFC list prepared successfully ({len(RFC_NUMBERS)} RFCs)')


if __name__ == '__main__':
    build_rfc_list()
