# Version 0.14

# 项目目的

这个项目中提供了pelican的初始设置和theme文件，以提供一个方便无痛的将jupyter notebooks发布成pelican blogs至git pages的体验。

尽管pelican中有ipynb插件，可以将ipybn文件转化成html，但是为了更好的支持用Jupyter撰写blog， 还需要做出大量的改进。主要的改进有:

* .ipynb文件往往不会孤立的出现， 它们一般要和静态文件，比如册书数据，图片等一起使用。它们最好能被用组织在一个相同的文件夹中。因此我们需要修改Pelicanconf.py的配置，让pelican能够识别放在文件夹中的.ipynb文件， 并且确保转化成html后链接依然有效。
* 由.ipynb转化的html中， 内容会被放在深层嵌套的<div>标签中，这样一些诸如tocify.js的javascript插件就没法正常生效了。所以需要在article的jinja2模板中添加一下javascript代码， 将从能从嵌套的<div>文件中提取出来。
* Pelican的'Clean_blog'主题提供了一个清爽，美观的视觉效果， 但是只提供了少量对于blog很重要的常见功能， 例如
    * 多说评论服务(中国disquas评论是被屏蔽的)
    * 自适应屏幕尺寸的侧边栏菜单
    * 分类，标签，归档菜单项
    * 微信打赏功能

# 演示
我的jupyter notebooks是放在[这里](https://github.com/junjiecai/jupyter_labs/tree/master/exolution)的, 你可以在[这里](https://junjiecai.github.io)看到它们被发布成blog以后的效果。

# 预备前置知识
If you have no idea about pelican and gitpages, please read one of these articles first.

* [Building a data science portfolio: Making a data science blog](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)
* [my blog on the same topic (Chinese)](http://junjiecai.github.io/posts/2016/Aug/10/blog_with_jupyter/)

如果你不知道pelican和gitpages是什么， 请先读一下下面两篇文章中的一篇。
* [Building a data science portfolio: Making a data science blog](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)
* [我自己的中文blog， 内容和上面一样](http://junjiecai.github.io/posts/2016/Aug/10/blog_with_jupyter/)

# 怎么使用这个项目
首先将这个项目clone到你的本地机器，然后完成后面的任务。

## 创建virtualenv(推荐)
如果没安装virtualenv的话，先安装一下
```
pip install virtualenv
```
将当前路径切换到项目文件夹，为它创建一个virtualenv。 建议使用python3.5或更高的版本。

```
virtualenv -p /usr/bin/python3.5 venv
```

激活虚拟环境

```
source venv/bin/activate
```

## 安装依赖包
创建一个requirements.txt， 然后填入以下内容。
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
然后运行

```
pip install -r requirements.txt
```

## 注册多说评论服务 (可选)
多说可以为你的blog提供评论模块。 如果需要的话，可以在[这里]((http://duoshuo.com/))注册一下多说服务, 记下多说域名(长得像XXXX.duoshuo.com')

## 注册google网站分析服务(可选)
在[这里](https://analytics.google.com/)为你的blog注册google网站分析服务，记下google analytics id (长得像'UA-xxxxxxxx-x')

## 创建customs.py
创建一个customs.py文件(放在和pelicanconf.py同级的文件夹下)， 然后添加以下内容

### 必填项目
```
AUTHOR = '你的名字'
SITENAME = "你的网站的名字"
SITEURL = "你的网站的url" # 例如, https://junjiecai.github.io 
ARTICLE_PATHS = ['articles'] # 相对于pelicanconf.py的相对路径， 制定了blog文章所在的位置。后面的例子会有详细说明。
```
### 选填项目
```
GOOGLE_ANALYTICS = 'UA-xxxxxxxx-x' # (可选) 激活google网站分析

WECHAT_PAYMENT_IMAGE = 'award.jpeg' # (可选) 可以在文章的最后添加一个微信付费的qrc图案。这里填的是在theme/static/customs/中支付qrc图片的文件名。

HEAD_COVER_IMAGE = 'bg-image.jpg' # (可选) 如果你愿意，可以把默认的封面图换掉。这里填的是在theme/static/customs/中header cover图片的文件名。

DUOSHUO_SITENAME = "your duoshuo site name" # (可选) 开启多说评论系统。如果你的duoshuo'XXXX.duoshuo.com', 这里就填'XXXX'

JUPYTER_BASE = 'base url' # (可选) 开启.ipynb源代码映射功能。后面的例子会有更多的说明。
```

### 关于设置项的进一步解释
#### ARTICLE_PATHS
举个例子，如果我们的文件夹结构是这样的

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
如果我们只想把文件夹labs_A和lifes下面的文章发布成blog，那么把ARTICLE_PATHS设置成
ARTICLE_PATHS = ['articles/jupyter_labs/labs_A','articles/lifes']

#### JUPYTER_BASE
有时候， 我们想将.ipynb文件和相关的资源文件push到github的一个repo中. 如果能自动的映射关联转化后的blog html和它对应的源文件链接， 那就很方便。 JUPYTER_BASE就是干这个用的。

如果JUPYTER_BASE设置正确， 每个从ipynb转化后的html的开头会被插入一段文字， 描述了源文件的位置。

例如，我有这样的文件夹结构的话

```
content
|   articles
    |   jupyter_labs
        |   exolution
            |   0000_blog_with_jupyter # 存放ipynb的文件夹
                |   0000_blog_with_jupyter.ipynb
                |   0000_blog_with_jupyter.ipynb-meta
|   pages
```

当我把jupyter_labs文件夹push到我的这个github repo后(https://github.com/junjiecai/jupyter_labs)， 指向0000_blog_with_jupyter.ipynb的url是

https://github.com/junjiecai/jupyter_labs/tree/master/exolution/0000_blog_with_jupyter
这个url可以被拆分成两部分

* 'https://github.com/junjiecai/jupyter_labs/tree/master/exolution/', 这部分在不同的.ipynb文件中是不会改变的. 它就是JUPYTER_BASE该填写的数值。
* 0000_blog_with_jupyter, 这时存放.ipynb文件和相关的资源的文件夹名. 他会被自动提取出来，添加到JUPYTER_BASE的后面，成为完整的路径。

## 创建content文件夹
在项目文件夹中建立一个叫做'content'的文件夹

## 为文章添加中文翻译
如果你想给文章添加英文翻译。用英语写另一篇.ipynb文件，使用同样的slug,但是把Lang设置成'en'。你可以在.ipynb文件中设置这些参数或者用前面介绍的模式命名文件，然后利用自动metadata提取功能。例如：
```
content
|   articles
    |   pytest_intro
        |   0001_pytest_intro_ch.ipynb
        |   0001_pytest_intro_ch.ipynb-meta
        |   0001_pytest_intro_en.ipynb
        |   0001_pytest_intro_en.ipynb-meta
```

当html生成额时候，就能在这些文章的开头看到语种切换按钮。

## 撰写文章
1. 创建一个文件夹(比如是ARTICLE_PATHS中定义过的路径的子文件夹)， 你可以为每一个blog单独建立一个文件夹。
2. 启动Jupyter Notebook,创建一个ipynb文件，写下你想写的内容。
3. 创建一个.ipynb-meta文件，提供关于你的blog的描述信息，例如id, 标题, 描述等等。.ipynb-meta文件的文件名必须和.ipybn文件一致。

之后，你会得到这样结构的文件夹

```
content
|   articles
    |   pytest_intro
        |   pytest_intro.ipynb
        |   pytest_intro.ipynb-meta

```

pytest_intro.ipynb-meta中的信息应该是这样的。

```Title: Pytest Introduction
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

'Id'是分配给每篇blog的一个id号， 对于每个语种下的blog，不同的文章的id号不能重复。不然像多说这样的评论系统会无法正常的工作。

'Lang'用来提供为文章提供额外的语种支持。看后面的例子了解详情。

Id, Slug, Lang的信息可以自动从文件名中被抽取出来， 只要他们是按照"<id>_<slug>_<lang>.ipynb"的模式去命名的。例如"0001_pytest_intro_ch.ipynb"的文件名定义了id = '0001', slug = 'pytest_intro' and lang = 'ch',这时就不用在.ipynb-meta files中在提供这些值了。

'Category'的值可以由每篇blog的content path之后第一级路径自动生成，例如， 如果我们有这样的文件结构。
```
content
|   articles
    |   pytest_intro
        |   0001_pytest_intro_ch.ipynb

```
那么pytest_intro的category就会被设定成'article', 除非你在.ipynb-meta中重新定义了别的值覆盖它。


## 添加页面
你可以在content/pages文件夹下添加诸如'关于我'之类的页面。它们的创建方式和文章是一样的。不过页面会出现在blog站点的菜单栏中， 而不是文章列表。

## git中添加指向gitpages的remote
```
git remote add blog git@github.com:[username]/[username].github.io.git
```
将[username]替换成你的github用户名

## 生成html然后把生成的html提交到gitpages
运行这三行命令然后欣赏你的blogs吧
```
pelican
ghp-import output -b master
git push blog master
```

** 记得运行pelican命令前， 删除掉.ipynb_checkpoints文件， 不然你会收到不少令人不爽的报错信息。**
