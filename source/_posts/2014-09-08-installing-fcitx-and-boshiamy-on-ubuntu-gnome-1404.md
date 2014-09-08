title: Installing Fcitx and Boshiamy on Ubuntu GNOME 14.04
date: 2014-09-08
tags: software
---

Fcitx 是一個自訂性很高的輸入法框架，安裝方式如下：

* Fcitx 框架
    ```bash
    sudo apt-get install fcitx
    ```

* 嘸蝦米輸入法表格
    ```bash
    sudo apt-get install fcitx-table-boshiamy
    ```

設定：

* `Activities` → `Input Method` 選擇 fcitx。重新登入。

* `Activities` → `Fcitx Configuration` → `Input Method` → `Boshiamy` → 雙擊
    `Other` → `Table` → `table/boshiamy.conf` → 設定
    `Adjust Order`：`AdjustNo`
    `Auto Send Candidate Word`：取消
    `Use Maching Key`：取消
    `Choose`：0123456789
    `Ignore Punctuation`：打勾

參考資料：

* [Ubuntu與嘸蝦米: 在fcitx下，(boshiamy)嘸蝦米的使用最為順暢、穩定!（新酷音、m17n、倉頡、輕鬆法亦適用）](http://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=246870)
