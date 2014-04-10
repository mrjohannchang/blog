Title: 在 Ubuntu 12.10 的 gcin 輸入法平台安裝嘸蝦米輸入法
Date: 2013-01-25 01:02
Tags: Software

## 步驟 1：安裝 gcin 及 im-switch

    :::sh
    sudo apt-get install gcin im-switch

## 步驟 2：指定預設輸入法平台為 gcin，完成後重新啟動電腦

    :::sh
    im-switch

## 步驟 3：下載並解壓縮嘸蝦米官方提供的 gcin 用表格，接著開啟終端機並進入解壓縮目錄

## 步驟 4：將表格等檔案複製到系統中

### 1. 前置作業

    :::sh
    sudo updatedb

### 2. 複製 \*.gtab 到 gcin 表格目錄

    :::sh
    sudo cp *.gtab $(locate gtab | grep gcin/table | while read line; do dirname "$line"; done | sort -u)

### 3. 複製 \*.png 到 gcin icon 目錄

    :::sh
    sudo cp *.png $(locate pinyin.png | grep gcin | while read line; do dirname "$line"; done | sort -u)

## 步驟 5：編輯 gtab.list

    :::sh
    echo "嘸蝦米(繁) 1 boshiamy-t.gtab boshiamy-t.png" >> ~/.gcin/gtab.list

## 步驟 6：重新啟動 gcin

## 步驟 7：調整 gcin 設定

### 1. 在【內定輸入法 & 開啟/關閉】中調整嘸蝦米是否為預設輸入法、可否由 ctrl + shift 切換

### 2. 在【倉頡/行列/嘸蝦米/大易設定】中將【預覽/預選 字】調整為【全部開啟】
