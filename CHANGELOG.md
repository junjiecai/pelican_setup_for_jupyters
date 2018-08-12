# Change Log
## 0.14
### improvement
* add chinese README

## 0.13.1
### improvement
* add lang and category infomation to DUOSHUO data-thread-key and DUOSHUO data-title

## 0.13
### New Features
* Category can be extracted from the first level path after content path for each article
* Side bar toc detect h1~t4 now
* Generated Site can be bilingual now (support Chinese and English).
* Hide ```div.prompt``` in generated HMTL for better visual effect.


## 0.12.1
### New Features
* Make wechat payment, DUOSHUO comments optional components and they can be configed in custom.py.
* Users can change header cover image through customs.py

### Refactoring
* html template for wechat payment, source code mapping are moved into indivisual template files.

### Bug fixes
* Directory name generated from date information always use english now.

## 0.11
### New Features
* Support JUPYTER_BASE config in customs.py to auto-append a paragraph in each article, linking to url containing related .ipybn file and other resources.


## 0.10.2
### Bug fixes
* Fix several text errors in readme.
* Fix tags page "404 not found" error.


## 0.10.1
### New Features
* Auto extract id and slug from filename if it's named with convention 'xxxx_slug'. They can be overwritten in the .ipynb-meta file.

### Bug fixes
* Fix several text errors in readme.
* Fix errors in pelicanconf.py






