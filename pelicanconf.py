#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

STATIC_PATHS = [ 'CNAME', 'images', 'scripts', 'extensions', 'icons', 'icons/favicon.ico', 'robots.txt', 'registrar']
PAGE_PATHS = ['registrar']
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
