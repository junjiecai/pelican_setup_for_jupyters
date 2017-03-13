# Version 0.14

# Project Goal
This project provides a initial pelican configs and theme files to offer a painless experience to publish jupyter notebooks as pelican blogs into gitpages.

Although pelican has ipynb plugin to convert .ipynb file into blog html, many adaptations have to be made to support jupyter notebook bloggin.

primary adaptations

* .ipynb files seldomly exist alone, they usually work with related static files such as test data, images, etc. They are better organized in  one same directorys. Pelicanconf.py is configured so that pelican can detect .ipynb files in directorys and the links are not broken after they are converted into html
* In .ipynb generated html, contents are nested deeply in <div> elements so some javascript plugins such as tocify.js cannot work properly. So scripts are added in article template to properly extract content from the nested <div> block
* 'Clean-blog' theme in pelican provides a clean, good looking but provide too little useful component common to blogs, such as
    * Duoshuo Comments (disqus is blocked for chinese users)
    * Responsive sidebar toc menu
    * Menus for category, tag, archives
    * Wechat award image

# Demonstration
My jupyter notebooks are kept in [here](https://github.com/junjiecai/jupyter_labs/tree/master/exolution)　and you can check what they look like after they are published into blogs [here](https://junjiecai.github.io)


# Perquisites
If you have no idea about pelican and gitpages, please read one of these articles first.

* [Building a data science portfolio: Making a data science blog](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)
* [my blog on the same topic (Chinese)](http://junjiecai.github.io/posts/2016/Aug/10/blog_with_jupyter/)


# How to use this project
After cloning the repo to your local machine, finish the following tasks


## create virtualenv (Recommended)
Install virtualenv if you don't have it
```
pip install virtualenv
```
Change directory into the project folder and create a virutalenv for it, python3.5 or higher is recommended

```
virtualenv -p /usr/bin/python3.5 venv
```

Activate the virtualenv

```
source venv/bin/activate
```

## install requirements
create a requirements.txt and put in the following lines
```
markdown
pelican==3.6.3
jupyter
ipython
nbconvert
beautifulsoup4
matplotlib
ghp-import
```

Then run

```
pip install -r requirements.txt
```


## Register DUOSHUO (Optional)
DUOSHUO provides comments module for your blogs. If you want it, register a DUOSHUO service [here](http://duoshuo.com/) for your blog and take note on your DUOSHUO site name. (looks like 'XXXX.duoshuo.com')


## Register Google Analytics(Optional)
Register a google analytics service [here](https://analytics.google.com/) for your blog site and take note on the google analytics id (looks like 'UA-xxxxxxxx-x')


## Create a customs.py
create a customs.py file (same folder with pelicanconf.py) and add the following content.


### Required Settings
```
AUTHOR = 'YourName'
SITENAME = "YourSiteName"
SITEURL = "YourSiteUrl" # For example, https://junjiecai.github.io 
ARTICLE_PATHS = ['articles'] # your article paths, relative to PATH in pelicanconf.py. See examples below for more detail.
```

### Optional Settings
```
GOOGLE_ANALYTICS = 'UA-xxxxxxxx-x' # (OPTIONAL) Enable google_analytics for your blog.

WECHAT_PAYMENT_IMAGE = 'award.jpeg' # (OPTIONAL) Enable wechat payment qrc at the bottom of each article. This is the filename for your wechat payment qrc image which should be put int theme/static/customs/ folder

HEAD_COVER_IMAGE = 'bg-image.jpg' # (OPTIONAL) Replace the default header cover image if you wish. This is the filename for your header cover   image which should be put int theme/static/customs/ folder

DUOSHUO_SITENAME = "your duoshuo site name" # (OPTIONAL) Enable DUOSHUO commenting. If your site name is 'XXXX.duoshuo.com', just fill in XXXX here

JUPYTER_BASE = 'base url' # (OPTIONAL) Provide this to enable auto source code mapping. See explaination below for more detail.
```


### More explanation about settings
#### ARTICLE_PATHS
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
|   pages
```

And we only want to publish contents in directory labs_A and lifes to blog posts, then set ARTICLE_PATHS as
ARTICLE_PATHS = ['articles/jupyter_labs/labs_A','articles/lifes']



#### JUPYTER_BASE
Sometimes, users wish to push the .ipynb files and related resource files into another repository on github. It's convient to automatically map blogs with urls pointing their source files in github. JUPYTER_BASE is used for this situation.

When JUPYTER_BASE is set properly. A automatically generated paragraph is inserted at the beginning of each blog after publishing.

For example, I have files structured like this

```
content
|   articles
    |   jupyter_labs
        |   exolution
            |   0000_blog_with_jupyter # folder name containing .ipynb file
                |   0000_blog_with_jupyter.ipynb
                |   0000_blog_with_jupyter.ipynb-meta
|   pages
```

After I push jupyter_labs directory (contains the source files) into my repository (https://github.com/junjiecai/jupyter_labs), the url pointing to 0000_blog_with_jupyter.ipynb is 

https://github.com/junjiecai/jupyter_labs/tree/master/exolution/0000_blog_with_jupyter

This url can be seperated into two parts

* 'https://github.com/junjiecai/jupyter_labs/tree/master/exolution/', which is invariant between articles. This is the value of JUPYTER_BASE
* 0000_blog_with_jupyter, folder name containing the .ipynb file and related resources. This is automatically extracted and appended into JUPYTER_BASE as the full url.



## Create content folder
Create a folder named with 'content' in the project folder


## Write articles
1. Create a folder (it must be subdirectory of paths defined in ARTICLE_PATHS), you can create one folder for each jupyter notebook lab.
2. Create a .ipynb file and write down the content you wish
3. Create a .ipynb-meta file to provide meta-data about your blog, such as id, title, description .etc, the .ipynb-meta file must has same filename with the .ipynb file

Then you should end up with the directories and files like this.
```
content
|   articles
    |   pytest_intro
        |   pytest_intro.ipynb
        |   pytest_intro.ipynb-meta

```

Within the pytest_intro.ipynb-meta, it should looks like this.
```
Title: Pytest Introduction

Date: 2016-08-15 21:05
Modified: 2016-08-15 21:05
Tags: python, testing
Category:jupyter_labs
Author: Exolution
Summary: Introduction for pytest
Id:0001
Slug: pytest_intro
Lang:ch
```

'Id' is a number assigned to each blog and should be kept unqiue among all blogs, or comments system like DUOSHUO won't work properly.

'Lang' is used to add bilingual language support of the articles. See explanation later.

Id, Slug, Lang can be automatically extracted from filenames of .ipynb if they are named with the pattern like "<id>_<slug>_<lang>.ipynb", for example, "0001_pytest_intro_ch.ipynb" defines id = '0001', slug = 'pytest_intro' and lang = 'ch'. Then you don't have to provide them in .ipynb-meta files.

'Category' be extracted from the first level path after content path for each article. For example, given the following structure
```
content
|   articles
    |   pytest_intro
        |   0001_pytest_intro_ch.ipynb

```
pytest_intro will have a category of 'article', unless you defined another value in .ipynb-meta and overwrite it.



## Add translations for articles
If you want to add english translation for an article. Write another .ipynb in English and set it with the same slug but lang equals to 'en'. You can set them in .ipynb-meta file or take advantage of the auto meda data extraction if you name your files with proper pattern. For example.
```
content
|   articles
    |   pytest_intro
        |   0001_pytest_intro_ch.ipynb
        |   0001_pytest_intro_ch.ipynb-meta
        |   0001_pytest_intro_en.ipynb
        |   0001_pytest_intro_en.ipynb-meta
```

When the html is generated, you will see a tranlation link at the header of the article.


## Add pages
You can add pages such as aboutme page, links page in content/pages. They are created in the same way with articles. But links for pages appear in the navigation menu instead of article list.


## Add your gitpages remote
```
git remote add blog git@github.com:[username]/[username].github.io.git
```
Replace [username] with your github username

## Generate html and push to gitpages
Run these three commands and enjoy your blogs.
```
pelican
ghp-import output -b master
git push blog master
```

** Don't forget to delete .ipynb_checkpoints files before run ```pelican``` command or else you will receive a lot of unpleasant error messages**

