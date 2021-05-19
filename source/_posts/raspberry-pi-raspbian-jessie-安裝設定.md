---
title: Raspberry Pi Raspbian Jessie 安裝設定
date: 2015-10-25 15:38:33
tags:
- devops
- sysadmin
---

Jessie 剛從 SysVinit 換成 systemd。因為不同的 init system 的設定方式不同，而 raspi-config 還沒有更新到支援 systemd，所以有些設定必須手動，不能透過 raspi-config。
<!-- more -->
<!-- toc -->
## 先嘗試從 raspi-config expand filesystem，以及其他設定，無效或沒有 UI 能操作的再嘗試下面的方法。

## 關閉開機自動啟動的 GUI (desktop)

```sh
sudo systemctl set-default multi-user.target
```

https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=92727

## 鍵盤 layout 由 enGB 改為 enUS

```sh
sudo dpkg-reconfigure keyboard-configuration
```

https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=80127

## Apt source 改為使用國網中心提供的 mirror

```txt
(ftp|http)://free.nchc.org.tw/raspbian/raspbian
```

https://www.raspbian.org/RaspbianMirrors

## 預設編輯器改為 Vim

```sh
sudo update-alternatives –config editor
```

https://www.raspberrypi.org/forums/viewtopic.php?f=27&t=9376

## 加入 SSH authorized key、關閉 pi user 的 password

## 設定 PPPoE

## 設定 DDNS (DNS provider -> (CNAME) -> twbbs.org -> (NS) -> FreeDNS

以前可以透過在 `/etc/network/if-up.d` 放一個可執行檔來hook DDNS 服務，但是現在 systemd 管理的 networking 似乎沒有辦法這麼做。

```sh
#!/bin/bash

set -e

ip=$(ip -f inet addr show eth0 | grep -Po 'inet \K[\d.]+')
( sleep 10 ; curl "https://url-to-update-ip-address" )
```

## 安裝 nvm、node

## 用 github-webhook-handler 寫一個 handler 來更新 blog。將 handler 加到 systemd service。

https://github.com/rvagg/github-webhook-handler
