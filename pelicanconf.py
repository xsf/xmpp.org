#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime, timedelta
import logging
import json

SITENAME = "XMPP"
SITE_URL = ""
TIMEZONE = "Europe/Paris"  #Unused (Pelican complains if you don't provide it)
DEFAULT_LANG = "en"

DEFAULT_METADATA = [
  ('top_menu_show', 'false'),
  ('top_menu_order', '-1'),
  ('dropdown_menu_show', 'false'),
  ('dropdown_menu_size', '0'),
  ('footer_show', 'false'),
  ('footer_order', '-1'),
  ('content_layout', 'single-column'),
  ('is_blog', 'false')
]

STATIC_PATHS = [ 'CNAME', 'images', 'scripts', 'extensions', 'icons', 'icons/favicon.ico', 'robots.txt', 'registrar', 'docs']
PAGE_PATHS = ['pages', 'registrar']
EXTRA_PATH_METADATA = {
  'icons/favicon.ico': { 'path': 'favicon.ico' }
}
DIRECT_TEMPLATES = [ 'index', 'categories', 'archives' ]
ARTICLE_PATHS = [ 'posts/blog', 'posts/learn' ]
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

INDEX_SAVE_AS = 'blog.html'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_PAGINATION = 10

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

THEME = "xmpp.org-theme"

MD_EXTENSIONS = [ 'codehilite(css_class=highlight)', 'extra' ]

FEED_MAX_ITEMS = 20
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

SWLISTS = {}

ENTRY_LIFETIME = timedelta(days=365)

# entires without renewal will be hidden after this point in time
STRICT_RENEWAL_DEADLINE = datetime(2017, 6, 1, 0, 0, 0)


def load_software_list(now, filename):
    """
    Load, preprocess and filter a software list from JSON.

    :param now: Used to determine whether software is still shown.
    :param filename: Filename in the ``data`` subdirectory to load.
    :return: List of dicts containing software information.

    * Software whose ``last_renewal`` is not null and older than
      :data:`ENTRY_LIFETIME` is omitted from the result.

    * Software whose ``last_renewal`` is none is removed after
      :data:`STRICT_RENEWAL_DEADLINE`.

    """

    with open("data/{}".format(filename), "r") as f:
        rows = json.load(f)

    result = []
    for row in rows:
        renewed = row.get("last_renewed")

        # has the software ever been renewed under the new system?
        if renewed is not None:
            try:
                renewed = datetime.strptime(renewed, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                logging.error(
                    "failed to parse timestamp; omitting entry %r",
                    row,
                )
                # parse error -> omit
                continue

            if now - renewed > ENTRY_LIFETIME:
                # renewal expired -> omit
                continue

        elif now > STRICT_RENEWAL_DEADLINE:
            # not renewed ever, also over deadline -> omit
            continue

        # set parsed timestamp
        row["last_renewed"] = renewed

        # put into result list
        result.append(row)

    return result


NOW = datetime.utcnow()
SWLISTS["libraries"] = load_software_list(NOW, "libraries.json")
SWLISTS["clients"] = load_software_list(NOW, "clients.json")
SWLISTS["servers"] = load_software_list(NOW, "servers.json")

with open("data/members.json", "r") as f:
    MEMBERLIST = json.load(f)

XEPS = []
