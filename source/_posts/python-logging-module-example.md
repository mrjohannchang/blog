title: Python logging module example
date: 2015-10-26 18:09:59
tags:
- programming
---

Python 的 logging module 功能完整強大，但手冊裡卻沒有一個簡明的 config 範例。

記錄一下。
<!-- more -->
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s|PID:%(process)d|TID:%(thread)d|%(filename)s:%(lineno)d|%(funcName)s|%(name)s|%(levelname)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': logging.DEBUG,
        },
        'http': {
            'class': 'logging.handlers.HTTPHandler',
            'formatter': 'default',
            'level': logging.DEBUG,
            'host': 'localhost:3000',
            'url': '/log',
        },
        'rotatingfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'level': logging.DEBUG,
            'filename': 'test.log',
            'maxBytes': 512 * 1024 * 1024,
            'backupCount': 1,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'http', 'rotatingfile'],
            'level': logging.DEBUG,
        },
    },
})

logging.info('test1')
logger = logging.getLogger()
logger.info('test')
```

## Ref

1. [The Hitchhiker’s Guide to Python]
2. [The Python Standard Library]

[The Hitchhiker’s Guide to Python]: http://docs.python-guide.org/en/latest/writing/logging/
[The Python Standard Library]: https://docs.python.org/2/library/logging.html
