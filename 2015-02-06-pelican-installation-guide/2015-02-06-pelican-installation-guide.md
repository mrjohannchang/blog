title: Pelican Installation Guide
date: 2015-02-06 23:24
authors: Chang Yu-heng
summary: A step-by-step guide for installing Pelican static site generator
about_author: An Android app developer
email: mr.changyuheng@gmail.com

1. Clone the [repo](https://github.com/murmuring-on-the-air/murmuring-on-the-air.github.io) recursively

        ::::sh
        git clone --recursive git@github.com:murmuring-on-the-air/murmuring-on-the-air.github.io.git

2. Change directory to the cloned repo

3. [Install Pelican](http://docs.getpelican.com/en/3.5.0/install.html)

    1. Creating virtual environments by Python venv

            ::::sh
            pyvenv venv
            source venv/bin/activate

        On Ubuntu 14.04 you might have to [install venv manually](http://askubuntu.com/q/488529) in advance

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

    2. Install Pelican and other stuff we needed

            ::::sh
            pip3 install -r requirements.txt
