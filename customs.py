


AUTHOR = 'Exolution'
SITENAME = "Exolution的奇妙冒险"
BASEURL='https://junjiecai.github.io'
SITEURL='https://junjiecai.github.io'
GITHUB_URL = 'https://github.com/junjiecai/jupyter_labs'
GOOGLE_ANALYTICS = 'UA-89522436-1'
ARTICLE_PATHS = ['articles/jupyter_labs/exolution']
JUPYTER_BASE = 'https://github.com/junjiecai/jupyter_labs/tree/master/exolution'
WECHAT_PAYMENT_IMAGE = 'award.jpeg'
HEADER_COVER_IMAGE = 'bg_image.jpg'


I18N_SUBSITES = {
    'en': {
        'SITENAME':"Exolution's Bizarre Adventure"
        }
    }


from os import listdir, getcwd
from shutil import rmtree
from os.path import join, isdir


cwd = getcwd()


STATIC_PATHS = []
for artical_path in ARTICLE_PATHS:
    STATIC_PATHS += [join(artical_path, blog_path) for blog_path in listdir(join(cwd, 'content', artical_path))]


def delete_cache_files():
    for path in ARTICLE_PATHS:
        for folder_name in listdir(join(cwd, 'content', path)):
            if isdir(join(cwd, 'content', path, folder_name)):
                for sub_folder_name in listdir(join(cwd, 'content', path, folder_name)):
                    if sub_folder_name.endswith('.ipynb_checkpoints'):
                        rmtree(join(cwd, 'content', path, folder_name, sub_folder_name))


delete_cache_files()


IPYNB_USE_METACELL = True
IGNORE_FILES = ['.ipynb_checkpoints']


