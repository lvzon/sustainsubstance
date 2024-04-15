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

#THEME = "pelican-elegant-1.3/"
THEME = "../elegant"

#PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']

#MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'subscript', 'superscript', 'sane_lists', 'smarty', 'headerid', 'toc']
#MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'subscript', 'superscript', 'sane_lists', 'smarty']

# see https://pythonhosted.org/Markdown/reference.html#markdown
# format required for Pelican 3.7
MARKDOWN = {
    'extension_configs': {
        # set linenums=True for line numbers
        # https://pythonhosted.org/Markdown/extensions/code_hilite.html
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        # on by default
        # see https://pythonhosted.org/Markdown/extensions/extra.html
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # https://facelessuser.github.io/pymdown-extensions/extensions/superfences/
        'pymdownx.superfences': {},
        # use single caret for superscript
        # use double caret for insertion (underline?)
        # https://facelessuser.github.io/pymdown-extensions/extensions/caret/
        'pymdownx.caret': {},
        # use single tildes for subscript
        # use double tildes for deletion
        # https://facelessuser.github.io/pymdown-extensions/extensions/tilde/
        'pymdownx.tilde': {},
        # https://pythonhosted.org/Markdown/extensions/smarty.html  
        'markdown.extensions.smarty': {},
        # so MathJax equations (always) make it through
        # https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/
        'pymdownx.arithmatex': {},
        # Auto-convert special symbols, like (tm) to ™
        # https://facelessuser.github.io/pymdown-extensions/extensions/smartsymbols/
        'pymdownx.smartsymbols': {},
    },
    'output_format': 'html5',
    'lazy_ol': False,
}

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

# Navbar setup, currently not supported by the Elegant theme: https://github.com/Pelican-Elegant/elegant/pull/733

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (
('NL', '//sustainsubstance.org/nl')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
