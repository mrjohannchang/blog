---
title: Cross Compiling Python 2.7.10 and 3.4.3 for MIPSel OpenWrt via uClibc with SSL and SQLite support
date: 2015-11-05 18:33:52
categories:
- Porting
---

The notes that were written after succeeding to cross compile Python 2.7.10 and 3.4.3 for MIPSel OpenWrt via uClibc.
<!-- more -->
I'm not gonna write a very detailed guide. I post my build script on the [GitHub](https://github.com/changyuheng/cpython-for-openwrt-mips/blob/3.4.3/build.sh), please leave a comment if you have any question.

## Build log (3.4.3)

{% gist 2e5b13276035fc1aa79a build.log %}

## Run test cases on the device (3.4.3)

```sh
bin/python3 lib/python3.4/test/test___all__.py
```

## Note

* 2.7.10 is 100% passed
* 3.4.3's xml.parsers.expat module will cause segmentation fault.

## Refs

1. [Cross Compiling Python for Embedded Linux](http://randomsplat.com/id5-cross-compiling-python-for-embedded-linux.html)

## Thanks to

[Cheng Wig](https://tw.linkedin.com/pub/cheng-wig/90/1a1/896), he showed me the positive attitude at work.
