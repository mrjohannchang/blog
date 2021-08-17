---
title: Port LEDE 17.01 to LinkIt Smart 7688
date: 2017-04-24
categories:
- 嵌入式
---

心血來潮幫忙把 LinkIt Smart 7688 的作業系統從 [OpenWrt Chaos Calmer 15.05.1](https://forum.openwrt.org/viewtopic.php?pid=315110) 升級到 [LEDE 17.01](https://lede-project.org/releases/17.01/)。

<!-- more -->

![](https://raw.githubusercontent.com/changyuheng/linkit-smart-7688-feed/master/.screenshots/greetings.png)

# Changelog

最重要的改變當然就是各個套件的版本變新了。像是：

1. Linux kernel 從 3.18 升級成 4.4.x。
2. Node 從 0.12.x 升級成 4.4.x。
3. 支援 Python 3.6（預編的 image 裡沒有放，要自己重新編譯或是透過 opkg 安裝）。

此外，這個版本才是真正的完全開源。本來 MediaTek 在 OpenWrt 上放的 Wi-Fi driver 是 closed source，如果 kernel 升級造成 driver 版本對不上，就只能祈禱 MediaTek 會釋出配合的新版 driver。不過從官方的 [issue list](https://github.com/MediaTek-Labs/linkit-smart-7688-feed/issues/37) 看來，目前 MediaTek 沒有再繼續維護這個 driver。

好在 OpenWrt 有開發一套完全開源的 Wi-Fi driver [mt76](https://github.com/openwrt/mt76) 給 MT7688 系列 chip 使用，所以這個 LEDE port 版本就採用這個 driver 了。

![](https://raw.githubusercontent.com/changyuheng/linkit-smart-7688-feed/master/.screenshots/wi-fi.png)

# Tweak

這個版本是我只稍微花一點時間做的玩票性質的東西，所以可能會有一些小問題。這些小問題就交給讀者再繼續努力了。

以下列出我已經測試的部分：

1. Serial console
2. Wi-Fi Access Point mode
3. 從 MediaTek 的網頁上設定 password。
4. SSH login
5. Python 2.7
6. Node 4.4.5

![](https://raw.githubusercontent.com/changyuheng/linkit-smart-7688-feed/master/.screenshots/website.png)

# Repository

Repository 連結在此：https://github.com/changyuheng/linkit-smart-7688-feed

照著 README 即可進行編譯。

也可以從這邊下載預編的 image：https://github.com/changyuheng/linkit-smart-7688-feed/releases/download/v0.1/lede-ramips-mt7688-LinkIt7688-squashfs-sysupgrade.bin
