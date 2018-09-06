


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


from os import listdir, getcwd, makedirs, remove
from shutil import rmtree, copyfile
from os.path import join, isdir, exists, isfile


cwd = getcwd()

month_mapping = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}

def get_file_info(full_path):
    file_name = full_path.split('/')[-1].split('.')[0]
    folder_name = file_name[:-3]
    lang_name = file_name[-2:]

    year = None
    title = None

    with open(full_path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('Date'):
                time_string = line.split(':')[1].strip()
                year, month, date = time_string[:10].split('-')
            elif line.startswith('Title'):
                title = line.split(':')[1].strip()
            else:
                pass
                                         


    return year, month, date, folder_name, lang_name, title

def get_nbdata_title(full_path):
    with open(full_path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('Title'):
                title = line.split(':')[1].strip()
    return title


def search_posts():
    data = []
    for artical_path_relative in ARTICLE_PATHS:
        artical_path_absolute = join(cwd, 'content', artical_path_relative)
        for post_folder_relative in listdir(artical_path_absolute):
            post_folder_absolute = join(cwd, 'content', artical_path_relative, post_folder_relative)
            if isdir(post_folder_absolute):
                image_paths_absolute = []
                post_paths_absolute = []
                for filename in listdir(post_folder_absolute):
                    file_path_absolute = join(post_folder_absolute, filename)
                    if filename.endswith('.ipynb_checkpoints'):
                        rmtree(file_path_absolute)
                    elif filename.endswith('.DS_Store'):
                        remove(file_path_absolute)
                    elif filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.jpg'):
                        image_paths_absolute.append(file_path_absolute)
                    elif filename.endswith('nbdata'):
                        year, month, day, post_folder_relative, lang_name, _ = get_file_info(file_path_absolute)
                        month = month_mapping[month]
                        if lang_name == 'ch':
                            target_folder = join(cwd, 'output', 'posts', year, month, day, post_folder_relative[5:])
                        else:
                            target_folder = join(cwd, 'output', 'en','posts', year, month, day, post_folder_relative[5:])
                        post_paths_absolute.append(target_folder)
                    else:
                        pass
                data.append((post_paths_absolute, image_paths_absolute))

    return data

def search_pages():
    data = []

    pages_path_absolute = join(cwd, 'content', 'pages')
    image_paths_absolute = []
    page_paths_absolute = []
    for filename in listdir(pages_path_absolute):
        file_path_absolute = join(pages_path_absolute, filename)
        if filename.endswith('.ipynb_checkpoints'):
            rmtree(file_path_absolute)
        elif filename.endswith('.DS_Store'):
            remove(file_path_absolute)
        elif filename.endswith('.jpeg') or filename.endswith('.png'):
            image_paths_absolute.append(file_path_absolute)
        elif filename.endswith('nbdata'):
            *_, lang_name, title = get_file_info(file_path_absolute)
            folder_name = '-'.join([s.lower() for s in title.split(' ')])
            if lang_name == 'ch':
                target_folder = join(cwd, 'output', 'pages', folder_name)
            else:
                target_folder = join(cwd, 'output', 'en','pages', folder_name)
            page_paths_absolute.append(target_folder)
        else:
            pass
    data.append((page_paths_absolute, image_paths_absolute))

    return data


# copy static image into output folder
def copy_image(data):
    for post_data, images in data:
        for target_folder in post_data:
            for image in images:
                src = image
                if not exists(target_folder):
                    makedirs(target_folder)
                target = join(target_folder, image.split('/')[-1])
                copyfile(src, target)


data = search_posts()
copy_image(data)

data = search_pages()
copy_image(data)
                                 




