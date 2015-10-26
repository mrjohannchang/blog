title: Python logging module example
date: 2015-10-26 18:09:59
tags:
- programming
coverImage: python-logging.png
---

Python 的 logging module 功能完整強大，但手冊裡卻沒有一個簡明的 config 範例。

記錄一下。
<!-- more -->
{% codeblock logging-example.py https://docs.python.org/2/library/logging.html logging %}
import logging
import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'f': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG,
        },
    },
    'loggers': {
        '': {
            'handlers': ['h'],
            'level': logging.DEBUG,
        },
    },
})

logging.info('logging')
logger = logging.getLogger()
logger.info('logger')
{% endcodeblock %}

## Ref

1. [The Hitchhiker’s Guide to Python]
2. [The Python Standard Library]

[The Hitchhiker’s Guide to Python]: http://docs.python-guide.org/en/latest/writing/logging/
[The Python Standard Library]: https://docs.python.org/2/library/logging.html
