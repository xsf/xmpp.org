'''
This file is used to download the XEP list and convert it to JSON
'''
from typing import Any

import sys
import os
import json

from defusedxml.ElementTree import fromstring
from defusedxml.ElementTree import ParseError
import requests

XEP_LIST_URL = 'https://xmpp.org/extensions/xeplist.xml'


def status_ok(status_code: int) -> bool:
    '''
    Status codes ranging from 200 (OK) to 300 (redirects) are okay
    '''
    if not 200 >= status_code < 400:
        return False
    return True


def build_xep_list() -> None:
    '''
    Download and parse xeplist.xml and build xeplist.json
    '''
    xeplist_request = requests.get(XEP_LIST_URL)
    if not status_ok(xeplist_request.status_code):
        sys.exit(f'Error while downloading xeplist.xml '
                 f'({xeplist_request.status_code}')

    try:
        root = fromstring(xeplist_request.content)
    except ParseError:
        sys.exit('Error while parsing xeplist.xml')

    def fix_status(status: str) -> str:
        if status == 'Draft':
            return 'Stable'
        return status

    xeps: list[dict[str, Any]] = []
    for xep in root.findall("xep"):
        if xep.get("accepted") == "true":
            xeps.append(
                {
                    'title': xep.find('title').text,
                    'status': fix_status(xep.find('status').text),
                    'number': int(xep.find('number').text),
                    'last_updated': xep.find('last-revision').find('date').text,
                    'type': xep.find('type').text,
                }
            )

    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    with open(f'{base_path}/../data/xeplist.json',
              'w',
              encoding='utf-8') as json_file:
        json.dump(xeps, json_file, indent=4)
    print('XEP List prepared successfully')


if __name__ == '__main__':
    build_xep_list()
