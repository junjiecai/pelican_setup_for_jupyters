#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Don't touch this

import sys
sys.path.append('')
import locale
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

from customs import *


MENUITEMS = [
            ('分类','categories.html'),
            ('标签','tags.html'),
            ('归档','archives.html')
        ]

I18N_SUBSITES['en']['MENUITEMS'] = [
            ('Categories','categories.html'),
            ('Tags','tags.html'),
            ('Archives','archives.html')
        ]


DUOSHUO_PREFIX = SITEURL.split(':')[1]
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives','tags']

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DATE_FORMATS = {
    'en': '%d/%m/%Y',
    'ch': '%Y-%m-%d'
}


PATH = 'content/'

PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = True


FILENAME_METADATA = '(?P<id>\d+)_(?P<slug>.*?)_(?P<lang>ch|en)'

PATH_METADATA = "articles/(?P<category>.*?)/(.*/)(?P<folder>.*)(/.*)"


ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

ARTICLE_ORDER_BY = 'reversed-id'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

LOAD_CONTENT_CACHE = False

TIMEZONE = 'Asia/Shanghai'

LOCALE = 'en_US.utf8'

DEFAULT_LANG = 'ch'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)



# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins']
PLUGINS = ['ipynb.markup','i18n_subsites']

#,'', 'extract_toc','neighbors','pdf'

## Theme Config for pelican-clean-blog
THEME = "themes"

HEADER_COVER = '../theme/images/home-bg.jpg'

COLOR_SCHEME_CSS = 'github.css'
