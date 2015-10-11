title: My Ubuntu GNOME Tweaks
date: 2014-04-23
tags:
- software
---

以 Ubuntu GNOME 14.04 LTS 英文語系為基礎。

<!-- more -->

## 安裝軟體

* [7z](#7z)
* [ClipIt](#clipit)
* [Fcitx](#fcitx)
* [Gnome Gmail](#gnome-gmail)
* [Java 8](#java8)
* [ubuntu-restricted-extras](#ubuntu-restricted-extras)
* [Vim](#vim)
* [VLC](#vlc)
* [文泉驛中文字型](#wen-quan-yi-fonts)
* [嘸蝦米輸入法](#boshiamy)

## Firefox 附加元件

* [Gmail Notifier](#gmail-notifier)
* [GNotifier](#gnotifier)

## 設定

* [APT](#apt)
* [Gnome Tweak Tool](#gnome-tweak-tool)
* [Input Method Configuration](#im-config)
* [Online Accounts](#online-accounts)

### <a name="7z"></a>7z

```sh
sudo apt install p7zip-full
```

### <a name="clipit"></a>ClipIt

剪貼簿管理程序，安裝的主要目的是要他同步剪貼簿的功能。因為 X11 的剪貼簿在「貼上」時，若來源程序已暫停或結束，會因無法讀取來源而無法貼上。可參考：[X Selections, Cut Buffers, and Kill Rings.](http://www.jwz.org/doc/x-cut-and-paste.html)
```sh
sudo apt install clipit
```

### <a name="fcitx"></a>Fcitx

```sh
sudo apt install fcitx
```

### <a name="gnome-gmail"></a>Gnome Gmail

讓預設郵件客戶端可被設定為 Gmail。
```sh
sudo apt install gnome-gmail
```

### <a name="java8"></a>Java 8

[Install Oracle Java 8 In Ubuntu Via PPA Repository](http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html)
```sh
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java8-installer
```

### <a name="ubuntu-restricted-extras"></a>ubuntu-restricted-extras

RAR、Flash Player 等非開源的程式之集合。
```sh
sudo apt install ubuntu-restricted-extras
```

### <a name="vim"></a>Vim

Vim with GNOME specific support.
```sh
sudo apt install vim-gnome
```

### <a name="vlc"></a>VLC

```sh
sudo apt install vlc
```

### <a name="wen-quan-yi-fonts"></a>文泉驛中文字型

開源的中文字型。
```sh
sudo apt install ttf-wqy-*
```

### <a name="boshiamy"></a>嘸蝦米輸入法

```sh
sudo apt install fcitx-table-boshiamy
```
需要 [Fcitx](#fcitx)。

### <a name="gmail-notifier"></a>Gmail Notifier

偵測到 Gmail 的新進信件時會由 Firefox 發出提醒。
[Gmail Notifier](https://addons.mozilla.org/zh-tw/firefox/addon/gmail-notifier-restartless/?src=search)

### <a name="gnotifier"></a>GNotifier

讓 Firefox 使用 GNOME、KDE、Xfce 或 OS X 桌面環境的提醒 (notification) 介面。
[GNotifier](https://addons.mozilla.org/zh-tw/firefox/addon/gnotifier/)

### <a name="apt"></a>APT

以國網中心的 APT 伺服器取代台灣大學的：將 `/etc/apt/sources.list` 內的 `tw.archive.ubuntu.com` 取代為 `free.nchc.org.tw`。

### <a name="gnome-tweak-tool"></a>Gnome Tweak Tool

依個人喜好調整預設設定。

### <a name="im-config"></a>Input Method Configuration

先安裝 [Fcitx](#fcitx)，接著由 `Activities` → `Input Method` 選擇 fcitx。

### <a name="online-accounts"></a>Online Accounts

由 `Activities` → `System Settings` → `Online Accounts` 登入 Google 帳戶，登入後可將右方不希望同步的功能關閉。若有開啟 Calendar 同步，可由螢幕最上方正中央的 Calendar 下拉選單中看到將近的活動，提醒時間到時也會由 Evolution 彈出視窗提醒。
