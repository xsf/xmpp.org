#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'members@xmpp.org'
SITENAME = u'XMPP Standards Foundation'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = "UA-1075750-10"

DIRECT_TEMPLATES = ['index']
THEME = 'xmpp.org-theme'
STATIC_PATHS = [ 'img', 'CNAME' ]
CUSTOM_CSS = 'theme/css/style.css'
BOOTSTRAP_THEME = 'journal'

# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra/custom.css', 'CNAME' ]

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}
