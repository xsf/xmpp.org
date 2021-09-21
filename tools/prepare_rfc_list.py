# This file is used to download RFC references and convert them to
# a single JSON file
import sys
import os
import json
import requests
import xml.etree.ElementTree as ET


def status_ok(status_code):
    # Status codes ranging from 200 (OK) to 300 (redirects) are okay
    if status_code >= 200 and status_code < 400:
        return True
    return False


rfc_numbers = [
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

basic_rfc_numbers = [
    6120,
    6121,
    7395,
    7590,
    7622
]

selfhosted_rfcs = [
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

bibxmlpath = 'https://xml2rfc.tools.ietf.org/public/rfc/bibxml'

rfcs = []

print('Start preparing RFC list')

for number in rfc_numbers:
    request = requests.get(f'{bibxmlpath}/reference.RFC.{number}.xml')
    if not status_ok(request.status_code):
        quit(f'Error while downloading reference for '
             f'RFC {number} ({request.status_code})')

    try:
        root = ET.fromstring(request.content)
    except Exception:
        quit(f'Error while parsing RFC reference for RFC {number}')

    authors = None
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

    obsoletes = None
    obsoleted_by = None
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

    basic = True if number in basic_rfc_numbers else False
    selfhosted = True if number in selfhosted_rfcs else False

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
    print(f'Added RFC {number}')

base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

with open(f'{base_path}/../data/rfc_list.json', 'w') as json_file:
    json.dump(rfcs, json_file, indent=4)

print(f'RFC list prepared successfully ({len(rfc_numbers)} RFCs)')
