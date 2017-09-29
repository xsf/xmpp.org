#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
import urllib2
import xml.etree.ElementTree as ET
from pelicanconf import *

# SITE_URL = "http://new.xmpp.org"
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

f = urllib2.urlopen("https://xmpp.org/extensions/xeplist.xml")
try:
    tree = ET.parse(f)
finally:
    f.close()

XEPS = [
    {
        "title": xep.find("title").text,
        "status": xep.find("status").text,
        "number": int(xep.find("number").text),
        "last_updated": xep.find("last-revision").find("date").text,
        "type": xep.find("type").text,
    }
    for xep in tree.getroot().findall("xep")
    if xep.get("accepted") == "true"
]
