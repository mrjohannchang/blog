# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chang Yu-heng (張昱珩)'
SITENAME = "A Programmer's Blog"
SITEURL = ''

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh'
LOCALE = 'en_US.UTF-8'

DEFAULT_CATEGORY = 'Blog'

MENUITEMS = (
        ('Archives', SITEURL + '/archives.html'),
        )

# Blogroll
LINKS = (
        ("JChien's Blog", 'http://jeffchien.github.io/'),
        ('qazq', 'http://qazq.pixnet.net/'),
        ('SAY something', 'http://sayuan.github.io/'),
        ("Yongjhih's Octopress Blog", 'http://yongjhih.github.io/'),
        )

# Social widget
SOCIAL = (
        ('Codeforces', 'http://codeforces.com/profile/changyuheng'),
        ('Facebook', 'https://facebook.com/mr.changyuheng'),
        ('Github', 'https://github.com/changyuheng'),
        ('LinkedIn', 'http://www.linkedin.com/pub/yu-heng-chang/56/583/6b8'),
        )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# static paths will be copied without parsing their contents
STATIC_PATHS = [
        'images',
        ]

GITHUB_URL = 'https://github.com/changyuheng'

THEME = 'themes/pelican-octopress-theme'
PLUGIN_PATH = 'plugins'
PLUGINS = ['render_math']

# Sepecific for Pelican Octopress Theme
LICENSE = '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a> This work by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Chang Yu-heng (張昱珩)</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.en_US">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br />'
