title: Cross Compiling Python 3.4.3 for MIPSel OpenWrt via uClibc with SSL and SQLite support
date: 2015-11-05 18:33:52
tags:
- devops
- programming
coverImage: mediatek-pcb.jpg
---

The notes that were written after succeeding to cross compile Python 3.4.3 for MIPSel OpenWrt via uClibc.

<!-- more -->

I'm not gonna write a very detailed guide. I post my build script on the [GitHub](https://github.com/changyuheng/cpython-for-openwrt-mips/blob/master/build.sh), please leave a comment if you have any question.

## Build log

{% gist 2e5b13276035fc1aa79a build.log %}

## Run test cases on the device

{% codeblock lang:bash %}
bin/python3 lib/python3.4/test/test___all__.py
{% endcodeblock %}

## Refs

1. [Cross Compiling Python for Embedded Linux](http://randomsplat.com/id5-cross-compiling-python-for-embedded-linux.html)

## Thanks to

[Cheng Wig](https://tw.linkedin.com/pub/cheng-wig/90/1a1/896), he showed me the positive attitude at work.
