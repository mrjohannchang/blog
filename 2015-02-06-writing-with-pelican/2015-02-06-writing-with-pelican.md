title: Writing with Pelican
date: 2015-02-06 23:44
authors: Chang Yu-heng
summary: Quickstart of writing with Pelican
tags: blog
about_author: An Android app developer
email: mr.changyuheng@gmail.com

![]({attach}pop.jpg)

1. Create a repo on Github for placing your article later

2. Add the repo to Git submodule

        ::::sh
        git submodule add --branch {branch_of_the_source_in_the_repo}  {repo_url} content/{id}

    E.g.

        ::::sh
        git submodule add --branch mota git@github.com:changyuheng/changyuheng.github.io.git content/changyuheng

3. Change the directory to content/{id}

4. Make a directory to contain the post source and other stuff such like images

    Check out [this](https://github.com/changyuheng/changyuheng.github.io/tree/mota) for example. Further information such as article metadata could be found [here](http://docs.getpelican.com/en/3.5.0/content.html).

5. Commit the changes in the submodule
