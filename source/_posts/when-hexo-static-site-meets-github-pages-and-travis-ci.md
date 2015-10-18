title: When Hexo Meets GitHub Pages and Travis CI plus Raspberry Pi
date: 2015-10-18 22:06:24
tags:
- software
- programming
---

JS 很有吸引力、Hexo 是台灣人寫的、速度比 Octopress 快、default 支援 GitHub Flavored Markdown，所以選 Hexo。

Hexo 是一個 static site generator，static site 是指 website 由 static web page 所組成。獲取 static web page 的 client 端得到的 web page，和儲存於 server 端的 web page 一模一樣，與 dynamic website 的 server 端即時產生 web page 傳送給 client 端不同。Static site server 端因此不需要具備即時生成不同 web page 的能力。
<!-- more -->
Travis-CI 提供了 hook GitHub repository event 的功能。開啟 hook 後，便會透過 repository 中的 .travis.yml 中的設定來執行。

GitHub repository 中，特定的 branch 會被自動當作 static web site 的內容來 render，render 的引擎是 Jekyll，因此可以放純 HTML 檔案也可以放 Jekyll 會 render 的檔案。

本來 Hexo 運作流程是，在 local 撰寫 Markdown 文章，完成後執從 Hexo 的命令來 render Markdown 檔案，生成 HTML 的 static web site，再將生成出來的目錄 push 到 GitHub repository 的特定 branch。

但是依賴 Hexo 有個缺點，在沒有裝 Hexo 的裝置，就沒辦法更新 web site 了。而 Hexo 的雖然也不是很難安裝，但是要裝東西就是麻煩，例如突然想要用手機或是平板來寫點東西，就會很困擾。

所以我們應該妥善運用網路上佛心來著的服務，像是 Travis CI。我們可以把透過 Hexo 產生 HTML 並 push 到 GitHub 這件事，丟到 Travis CI 上面做。Hook Travis CI 很簡單，其他地方也有教學了。這篇文章的重點是在於，介紹一個 tricky 的方法來 push。

GitHub 支援 token 認證，token 就像是另一把隨時可以被回收鑰匙，透過 token 就可以有 write repository 的權限。可是很可惜的，目前 GitHub 沒有提供單獨為某一個 repository 產生一個 token 的服務，每一個 token 都能 write GitHub 帳號下的所有 repository。這實在有點恐怖。還好 GitHub 支援每一個 repository 擁有個別的 SSH public key。所以重點來了，我們該怎麼讓 Travis CI 擁有 SSH key pair 呢？總不能大剌剌的把 key pair 放在 repository 裡吧？免費的 repository 都是公開的，這樣做也太搞笑了。另一種方法是，先把 SSH key 加密再放進 repository，然後把密碼寫在 Travis CI 的環境變數裡，讓 Travis CI runtime 把 key 解回來。以上二種方法是網路上各路人馬目前廣泛使用的。

上面這二種方法都要用到 Travis CI 的環境變數，我實在很納悶，何不直接把 SSH key pair 當成變數就好了？也許是因為 public key 的內容含有空白和換換及其他特殊字元，這些字元在 runtime 直接 assign 給 shell 的 variable 會發生與期待不符的結果吧。這邊要說的 tricky 方法就是，把那二把 key 先用 Base64 encode，這樣就可以正確 assign 給 shell 的 variable，runtime 再把 variable decode 回 key file。這樣這個流程就能順利走完了！我們可以直接在 GitHub 網頁上編輯 Markdown，讓 GitHub 網頁幫我們 push、Travis CI 幫我們執行 Hexo 來 render 並且 push。

接著，因為剛好有閒置的樹莓派，我索性把 static site 就放在樹莓派上。所以上面這個自動化流程還必須涵蓋到更新樹莓派上面的內容。剛好 GitHub 有 webhook，當 repository 更新時，webhook 會發 http request 出去。GitHub 上有現成的 webhook handler，抓下來設定一下，放在樹莓派上面跑，這樣就可以自動更新 website 了。

Refs

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
