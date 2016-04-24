#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Levien van Zon'
SITENAME = u'The Substance of Sustainability'
#SITEURL = 'http://192.168.254.5/levien.zonnetjes.net/duurzaamheid'
#SITEURL = 'http://levien.zonnetjes.net/duurzaamheid'
SITEURL = ''

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'nl'
DEFAULT_DATE = 'fs'

#TYPOGRIFY = True

THEME = "pelican-elegant-1.3/"

#PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'subscript', 'superscript', 'sane_lists', 'smarty', 'headerid', 'toc']
#MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'subscript', 'superscript', 'sane_lists', 'smarty']

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images', 'files', 'offline']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

SITE_LICENSE = 'Except where otherwise noted, content on this site is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.'
#SITE_DESCRIPTION = 'duurzaamheidsweb.nl'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

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
