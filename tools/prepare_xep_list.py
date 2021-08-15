# This file is used to download the XEP list and convert it to JSON
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


xeplist_request = requests.get("https://xmpp.org/extensions/xeplist.xml")
if not status_ok(xeplist_request.status_code):
    quit(f'Error while downloading xeplist.xml ({xeplist_request.status_code}')

try:
    root = ET.fromstring(xeplist_request.content)
except Exception:
    quit('Error while parsing xeplist.xml')

xeps = []
for xep in root.findall("xep"):
    if xep.get("accepted") == "true":
        xeps.append(
            {
                "title": xep.find("title").text,
                "status": xep.find("status").text,
                "number": int(xep.find("number").text),
                "last_updated": xep.find("last-revision").find("date").text,
                "type": xep.find("type").text,
            }
        )

base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

with open(f'{base_path}/../data/xeplist.json', 'w') as json_file:
    json.dump(xeps, json_file, indent=4)
print('XEP List prepared successfully')
