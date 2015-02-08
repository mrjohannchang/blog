撰寫說明
########

:date: 2015-02-06 23:44
:tags: blog
:authors: Chang Yu-heng
:summary: 一樣是個手把手的教學
:about_author: An Android app developer
:email: mr.changyuheng@gmail.com

.. image:: {attach}pop.jpg

1. cd 到部落格的根目錄

2. 載入 venv 目錄中的虛擬環境

   .. code-block:: sh

      source venv/bin/activate

3. cd 到文章 source code 的目錄

   .. code-block:: sh

      cd content/{username}

4. 開一個目錄來裝文章並切進去

   .. code-block:: sh

      mkdir 2015-02-06-hello-world
      cd 2015-02-06-hello-world

5. 創建文章 (支援 Markdown 和 reST，這邊以 Markdown 為例) 並開始編輯

   .. code-block:: sh

      touch 2015-02-06-hello-world.md
      editor 2015-02-06-hello-world.md

6. 填寫文章的 metadata，接著開始撰內容

   .. code-block:: text

      title: 這是標題
      date: 2015-02-06 23:24
      authors: 作者的名字
      summary: 副標題
      tags: 用 , 分隔的標籤們
      about_author: 簡短的作者介紹
      email: 作者的 email

      文章內容參上！

7. 寫完之後記得存檔，然後回到部落格根目錄生成 html

   .. code-block:: sh

      make html

8. 在自己的電腦上開一個 HTTP server 來看看結果

   .. code-block:: sh

      make serve

   用瀏覽器打開 http://localhost:8000/

9. Ctrl-c 中止 server 執行

10. 到文章所在的目錄把文章 commit 並 push，再到部落格根目錄把文章 repo 的變動 commit 並 push

   .. code-block:: sh

      cd content/{username}
      git commit -am "My super post"
      git push
      cd ../..
      git commit -am "Update {username}'s post"
      git push

11. 發佈到 GitHub 上

   .. code-block:: sh

      make github

更多說明：

- `官方說明`_
- changyuheng 文章的 `source code`_

.. _官方說明: http://docs.getpelican.com/en/3.5.0/content.html
.. _source code: https://github.com/changyuheng/changyuheng.github.io/tree/mota
