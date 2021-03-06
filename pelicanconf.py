#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tracy Poff'
SITENAME = u'Other Stuff Exists'

THEME= 'foundation-default-colours'

PATH = 'content'
STATIC_PATHS = ['images']

OUTPUT_PATH = 'output'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

MD_EXTENSIONS = ['codehilite','extra',]

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Live Site (Wordpress)', 'http://otherstuffexists.wordpress.com/'),
        )

# Social widget
SOCIAL = (('@TracyPoff', 'https://twitter.com/TracyPoff'),
         )

DEFAULT_PAGINATION = 10

DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
