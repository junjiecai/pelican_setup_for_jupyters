#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Don't touch this

import sys
sys.path.append('')
from customs import AUTHOR, SITENAME, DUOSHUO_PREFIX,ARTICLE_PATHS,DUOSHUO_SITENAME,GITHUB_URL,GITHUB_URL,GOOGLE_ANALYTICS

AUTHOR = 'Exolution'
SITENAME = "Exolution's Blog"
SITEURL = ''
DUOSHUO_PREFIX = 'junjiecai.github.io'

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DATE_FORMATS = {
    'en': '%d/%m/%Y'
}


PATH = 'content/'
MENUITEMS = [
    ('分类','categories.html'),
    ('标签','tags.html'),
    ('归档','archives.html')
]
PAGE_PATHS = ['pages']

DISPLAY_PAGES_ON_MENU = True


ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

ARTICLE_ORDER_BY = 'reversed-id'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

LOAD_CONTENT_CACHE = False

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

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
PLUGINS = ['ipynb.markup']

#,'', 'extract_toc','neighbors','pdf'

## Theme Config for pelican-clean-blog
THEME = "themes"

HEADER_COVER = '../theme/images/home-bg.jpg'

COLOR_SCHEME_CSS = 'github.css'
