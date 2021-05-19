---
title: When Hexo Meets GitHub Pages and Travis CI plus Raspberry Pi
date: 2015-10-18 22:06:24
categories:
- Setup
---

JS 很有吸引力、Hexo 是台灣人寫的、速度比 Octopress 快、default 支援 GitHub Flavored Markdown，所以選 Hexo。
<!-- more -->
Hexo 是一個 static site generator，static site 是指 website 由 static web page 所組成。獲取 static web page 的 client 端得到的 web page，和儲存於 server 端的 web page 一模一樣。與 dynamic website 的 server 端即時產生 web page 傳送給 client 端不同，static site 的 server 端不需要具備即時生成不同 web page 的能力。

Travis-CI 提供了 hook GitHub repository event 的功能。開啟 hook 後，便會依照 repository 裡 .travis.yml 內的設定來執行。

GitHub repository 特定的 branch 會被 GitHub 當作 static web site 的內容來 render，render 的引擎是 Jekyll，因此可以放純 HTML 檔案也可以放 Jekyll 會 parse 的檔案。

本來 Hexo 的運作流程是，在 local 用 markup 撰寫文章，完成後執行 Hexo 的命令來 parse 並 render 原始檔案，生成由 HTML 構成的 static web site，再將生成出來的內容 push 到 GitHub repository 的特定 branch。

但是依賴 local Hexo 指令有個缺點：在沒有裝 Hexo 環境的裝置就沒辦法更新 web site 了。Hexo 環境雖然也不是很難安裝，但是要裝東西就是麻煩，尤其是突然有點靈感想要用手機或平板來寫點東西時特別困擾。

所以我們應該妥善運用網路上佛心來著的服務，像是 Travis CI。我們可以把透過 Hexo 產生 HTML 並 push 到 GitHub 這個流程，丟到 Travis CI 上，讓它來代理。Hook Travis CI 很簡單，其他地方也有專門針對 Hexo 的教學了。這篇文章的重點是在於，介紹一個 tricky 的方法來 push。

GitHub 支援 token 認證，token 就像是另一把隨時可以被回收鑰匙，透過 token 就可以有 write repository 的權限。可是很可惜的，目前 GitHub 沒有提供為個別的 repository 產生 token 的服務，每一個 token 都能 write GitHub 帳號下的所有 repository。這實在有點恐怖。還好 GitHub 支援每一個 repository 單獨設定 SSH public key 認證。所以重點來了，我們該怎麼讓 Travis CI 擁有 SSH key pair 呢？總不能大剌剌的把 key pair 放在 repository 裡吧？免費的 repository 都是公開的，這樣做也太搞笑了。另一種方法是，先把 SSH key 加密再放上 Travis CI，把密碼寫在 Travis CI 的環境變數裡，讓 Travis CI runtime 再把 key 解出來。目前網路上只看到這二種做法。

不過上面這二種方法都有用到 Travis CI 的環境變數，我實在很納悶，何不直接把 SSH key pair 當成變數就好了？也許是因為 public key 的內容含有空白和換行及其他特殊字元，這些字元在 runtime 直接 assign 給 shell 的 variable 會發生與期待不符的結果吧。這邊要說的 tricky 方法就是，把那二把 key 先用 Base64 encode，這樣就可以正確 assign 給 shell 的 variable，runtime 再把 variable decode 回 key file。這樣這個流程就能順利走完了！

以後我們就可以直接在 GitHub 網頁上編輯 Markdown 檔案，讓 GitHub 網頁來幫我們 push、Travis CI 幫我們 render 和 push。也可以搭配其他線上的所見即所得編輯器，有些編輯器還可以連結 GitHub 帳號。總之這樣以後就可以只管專心寫文章，不必做 routine 的事。

接著，因為剛好有閒置的樹莓派，我索性把 static site 放在樹莓派上。所以上面這個自動化流程還必須涵蓋到更新樹莓派上面的內容。剛好 GitHub 有提供 webhook 服務，當 repository 更新時，GitHub webhook 會發 http request 出來。GitHub 上有網友寫好現成的 webhook handler，抓下來設定一下，放在樹莓派上面跑，這樣就可以透過 GitHub 的 request 來 trigger 自動更新 website 了。

## 參考資料

1. [Using Jekyll with Pages](https://help.github.com/articles/using-jekyll-with-pages/)
2. [Hexo 颯爽登場！](http://zespia.tw/blog/2012/10/11/hexo-debut/)
3. [node-github-hook](https://github.com/nlf/node-github-hook)
4. [github-webhook-handler](https://github.com/rvagg/github-webhook-handler)
5. [用 Travis CI 自動部署網站到 GitHub](http://zespia.tw/blog/2015/01/21/continuous-deployment-to-github-with-travis/)
6. [我的 .travis.yml](https://github.com/changyuheng/changyuheng.github.io/blob/hexo3/.travis.yml)
7. [Top Open-Source Static Site Generators](https://www.staticgen.com/)
8. [Travis CI](https://travis-ci.org/)
9. [GitHub Webhooks](https://developer.github.com/webhooks/)
10. [樹莓派](https://www.wikiwand.com/zh-tw/%E6%A0%91%E8%8E%93%E6%B4%BE)
11. [公開金鑰加密](http://www.wikiwand.com/zh-tw/%E5%85%AC%E5%BC%80%E5%AF%86%E9%92%A5%E5%8A%A0%E5%AF%86)
12. [Encryption keys](http://docs.travis-ci.com/user/encryption-keys/)
