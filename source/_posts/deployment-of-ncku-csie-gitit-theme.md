title: Deployment of NCKU CSIE Gitit Theme
date: 2010-04-22
tags:
- software
---

[Gitit](http://gitit.net/) 是一套以 Git 作為 base 的 wiki 系統。這套 wiki 的優點可以在[只放拖鞋的鞋櫃](http://walkingice.blogspot.tw/2011/11/gitit-git-based-wiki.html)看到。在網路上的高手 [Macropodus](http://macropodus.github.io/gitit_mix_vimwiki.html) 研究出如何和 Vimwiki 結合後，又更強化了他的優勢。

不過 Gitit 預設的模版很沒有設計感，尤其是那個 logo 讓人看了很不舒服。所幸在 [Google Group](https://groups.google.com/forum/#!topic/gitit-discuss/g6rZWIOmiu8) 發現了一套由成大資工所製作的好看佈景。以下將介紹如何安裝這套佈景：

<!-- more -->

1. 下載佈景
打包好的佈景可以在 [GitHub](https://github.com/CrBoy/csiewiki) 上找到

2. 安裝佈景
將包裏解開後，取代 Gitit 原來的 static 和 templates 資料夾

到此為止都和這套佈景的官方安裝教學一樣。如果是採用發行版如 Ubuntu 所提供的 Gitit package，則已經完成。若是用 cabal 安裝, 則必須再安裝相依的套件，以 Ubuntu 為例：

```sh
sudo apt-get install libghc-filestore-data libc6 libffi6 libgmp10 libpcre3 zlib1g libjs-jquery libjs-jquery-ui
```

完成的樣子可以參考[成大資工 Wiki](http://wiki.csie.ncku.edu.tw/)。
