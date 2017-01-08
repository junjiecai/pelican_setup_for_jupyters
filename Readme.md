# Project Goal
This project provides a initial pelican configs and theme files to offer a painless experience to publish jupyter notebooks as pelican blogs into gitpages.

Although pelican has ipynb plugin to convert .ipynb file into blog html, many adaptations have to be made to support jupyter notebook bloggin.

primary adaptations

* .ipynb files seldomly exist alone, they usually work with related static files such as test data, images, etc. They are better organized in  indivisual directorys. Pelicanconf.py is configured so that pelican can detect .ipynb files in directorys and the links are not broken after they are converted into html
* In .ipynb generated html, contents are nested deeply in <div> elements so some javascript plugins such as tocify.js cannot work properly. So scripts are added in article template to properly extract content from the nested <div> block
* 'Clean-blog' theme in pelican provides a clean, good looking but provide too little useful component common to blogs, such as
    * Duoshuo Comments (disqus is blocked for chinese users)
    * Responsive sidebar toc menu
    * Menus for category, tag, archives
    * Wechat reward image

# Demonstration
My jupyter notebooks are kept in [here](https://github.com/junjiecai/jupyter_labs/tree/master/exolution)　and you can check what they look like after they are published into blogs [here]((https://junjiecai.github.io)

# Perquisites
If you have no idea about pelican and gitpages, please read one of these articles first.

* [Building a data science portfolio: Making a data science blog](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)
* [my blog on the same topic (Chinese)](http://junjiecai.github.io/posts/2016/Aug/10/blog_with_jupyter/)

# How to use
After cloning the repo to your local machine, finish the following tasks

## Register DUOSHUO 
Register a DUOSHUO service [here](http://duoshuo.com/) for your blog and take note on your DUOSHUO site name. (looks like 'XXXX.duoshuo.com')

## Register Google Analytics
Register a google analytics service [here](https://analytics.google.com/) for your blog site and take note on the google analytics id (looks like 'UA-xxxxxxxx-x')

## Create a custom.py
create a custom.py file (same folder with pelicanconf.py) and add the following content
```
AUTHOR = 'YourName'
SITENAME = "YourSiteName"
DUOSHUO_PREFIX = 'YourSiteUrl'
DUOSHUO_SITENAME = <your duoshuo site name> #If your site name is 'XXXX.duoshuo.com', just fill in XXXX here
GITHUB_URL = <your github url>
GOOGLE_ANALYTICS = 'UA-xxxxxxxx-x' #Your google analytics id
ARTICLE_PATHS = ['articles'] # your article paths, relative to PATH in pelicanconf.py. See examples below

```

For example, here we have files structured like this

```
content
|   articles
    |   jupyter_labs
        |   labs_A
            |   article_0
                |   article0.ipynb
                |   article0.ipynb-meta
            |   article_1
                |   article1.ipynb
                |   article1.ipynb-meta
        |   labs_B

    |   lifes
        |   article_2
            |   article2.ipynb
            |   article2.ipynb-meta
|   posts
```

And we only want to publish contents in directory labs_A and lifes to blog posts, then set ARTICLE_PATHS as
```
ARTICLE_PATHS = ['articles/jupyter_labs/labs_A','articles/lifes']
```

## Replace images
Images are stored under "/themes/pelican-clean-blog/static/images"

* home-bg.jpg: Used for blog background
* award.jpeg: Used for wechat payment qr code image at the bottom of each article. I appreciate it very much if you keep my payment qr code:)

## Compose your jupyter notebook
1. Create a folder (it must be subdirectory of paths defined in ARTICLE_PATHS), you can create one folder for each jupyter notebook lab.
2. Create a .ipynb file and write down the content you wish
3. Create a .ipynb-meta file to provide meta-data about your blog, such as id, title, description .etc, the .ipynb-meta file must has same filename with the .ipynb file


For example: 
If I want write down a jupyter notebook about pytest, then I end up with the following folder and files

```
pytest_intro
|   pytest_intro.ipynb
|   pytest_intro.ipynb-meta
```

Within the pytest_intro.ipynb-meta, it should looks like this.
```
Title: Pytest Introduction
Slug: pytest_intro
Date: 2016-08-15 21:05
Modified: 2016-08-15 21:05
Tags: python, testing
Category:jupyter_labs
Author: Exolution
Id:0001
Summary: Introduction for pytest
```

'Id' is a number assigned to each blog and should be kept unqiue among all blogs, or comments system like DUOSHUO won't work properly.

## Generate html and push to gitpages
Run these three commands and enjoy your blogs.
```
pelican
ghp-import output -b master
git push origin master
```

*** Don't forget to delete .ipynb_checkpoints files before run ```pelican``` command***


