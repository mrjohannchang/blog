title: 本部落格開發、撰寫環境安裝說明
date: 2015-02-06 23:24
authors: 張昱珩
summary: 手把手的安裝教學
tags: blog
about_author: 一位 Android app 開發人員
email: mr.changyuheng@gmail.com

![]({attach}ayanami-rei.jpg)

## 安裝開發環境

1. 在想要的目錄把部落格的 [repo](https://github.com/murmuring-on-the-air/murmuring-on-the-air.github.io) 遞迴地 clone 回來

        ::::sh
        git clone --recursive git@github.com:murmuring-on-the-air/murmuring-on-the-air.github.io.git

2. cd 進 clone 回來的 repo 目錄

3. 安裝本部落格用的靜態網站產生器 [Pelican](http://docs.getpelican.com/en/3.5.0/install.html)

    1. 首先用 Python 的 [venv][venv_link] 初始化一個虛擬環境，其中 `pyvenv venv` 是在當前目錄建立一個名為 `venv` 的目錄作為 [venv][venv_link] 所需工作目錄之用，`source venv/bin/activate` 則是載入這個 `venv` 的虛擬環境。

            ::::sh
            pyvenv venv
            source venv/bin/activate

        目前的 Ubuntu 14.04 中的 venv 套件是壞的，用這個版本發行版的讀者，若發現上面的指令執行不正常，請改用下面的方法[手動安裝](http://askubuntu.com/q/488529)：

            ::::sh
            pyvenv-3.4 --without-pip venv
            source ./venv/bin/activate
            wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz
            tar -vzxf setuptools-3.4.4.tar.gz
            cd setuptools-3.4.4
            python setup.py install
            cd ..
            wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz
            tar -vzxf pip-1.5.6.tar.gz
            cd pip-1.5.6
            python setup.py install
            cd ..
            deactivate
            rm -rf setuptools-3.4.4* pip-1.5.6*
            source ./venv/bin/activate

    2. 安裝 [Pelican](http://docs.getpelican.com/en/3.5.0/install.html) 和他相依的 library

            ::::sh
            pip3 install -r requirements.txt

<br />
## 安裝撰寫環境

1. 在自己的 GitHub 或是任何 Git hosting 開一個 repo，以便存放文章的 source code

2. 在自己的電腦上，cd 到部落格開發環境的根目錄，把剛開好的 repo 加進部落格的 repo 中。

        ::::sh
        git submodule add --branch {branch 名稱}  {repo 位置} content/{自己的 username}
        git commit content/{自己的 username}

    範例：

        ::::sh
        git submodule add --branch mota git@github.com:changyuheng/changyuheng.github.io.git content/changyuheng
        git commit content/changyuheng

[venv_link]: https://docs.python.org/3/library/venv.html
