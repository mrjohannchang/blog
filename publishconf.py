# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://changyuheng.github.io'
RELATIVE_URLS = False

SEARCH_BOX = True
SITESEARCH = 'https://google.com/search'

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "aprogrammersblog"
GOOGLE_ANALYTICS = "UA-44162683-1"

# Following items are often useful when publishing
