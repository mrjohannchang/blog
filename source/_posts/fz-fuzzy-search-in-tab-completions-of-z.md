---
title: fz - 模糊搜尋互動式 cd 自動補完套件
date: 2017-04-12 11:10:53
categories:
- 軟體
---

![](https://raw.githubusercontent.com/changyuheng/fz/master/fz-demo.gif)

<!-- more -->

在開始介紹之前，推薦大家先看看下面這篇文章：

[命令行上的narrowing（随着输入逐步减少备选项）工具](http://www.cnblogs.com/bamanzi/p/cli-narrowing-tools.html)

不知道大家會不會常常在 cd 路徑的時候，只大概記得在哪裡或是記得在哪裡但是目錄很深懶得打完全部的路徑。

這個時候 [fzf](命令行上的narrowing（随着输入逐步减少备选项）工具) 就很好用：

只要執行 `cd **<TAB>` 即可叫出互動式模糊搜尋介面，找到目標之後按二次 `<ENTER>` 就可以進入該目錄。

但是它有一個缺點，就是雖然它有快取也已經很快，而且還讓你用 [ag](https://github.com/ggreer/the_silver_searcher)  或 [pt](https://github.com/monochromegane/the_platinum_searcher) 把 `find` 換掉來讓它依 CPU thread 數平行遍歷目錄變得更快；當搜尋的範圍中有 AOSP (Android 的 source code) 這種大咖時，還是慢；就算不慢，資訊量也太大了。

於是乎，有人就想，如果能替曾經去過的目錄們建 MRU 表，以後切目錄時，如果確定有去過，從這張表搜尋就好，就會很快資訊量也不會太大。

這個功能有好幾個人做，目前最有名的是 [z](https://github.com/rupa/z)。

但是 z 雖然也有支援 tab completion，可是它只支援 substring filter，而且不是互動的。

z 在超強的 [fish](https://github.com/fish-shell/fish-shell) 下使用倒是還好，因為 fish 的選單有互動搜尋介面，不過這是當然的，因為它就是主打這個功能才會叫 friendly interactive shell 啊！

可是 fish 沒事幹嘛改 syntax 呢……

還有 process substitution ㄌㄟ？

所以大多數人還是繼續用 Bash 或 zsh。而且 zsh 有一個知名的 framework 叫 oh-my-zsh，把它裝下去之後就能讓你的 zsh 跟 fish 有 87% 那麼像啊！

但是！就是這個但是讓我花了點時間！它的 tab completion 還是不能互動搜尋啊！
我知道有人想說 [zaw](https://github.com/zsh-users/zaw) 對不對？

可是 zaw 的選單不是 **TAB** completion 啊！

目前為止，有 z 有 fzf，材料都齊了，就是沒人把它們兜在一起。於是我犧牲了一點寶貴的週末把它們逗起來，示意圖就是本文開頭那張 gif。

如果你覺得不錯，這個工具解決了你的問題，可以參考這個[安裝說明](https://github.com/changyuheng/fz/blob/master/README-zh.md)安裝。
