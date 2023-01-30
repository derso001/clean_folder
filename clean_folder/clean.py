import os
import sys
import shutil

#python clean.py C:\Users\zdoro\Desktop\мотлох
#python E:\python\clean_folder\clean_folder\clean.py C:\Users\zdoro\Desktop\мотлох
#clean-folder C:\Users\zdoro\Desktop\мотлох

arg = sys.argv[1]
PATH = f'{arg}'
#PATH = r'C:\Users\zdoro\Desktop\мотлох'
my_dirs = ['images', 'documents', 'audio', 'video', 'archives', 'unknown']
path = PATH
result = {
        'documents':[''],
        'audio':[''],
        'images':[''],
        'video':[''],
        'archives':[''],
        'unknown':['']
    }


########################

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

symbols = '~@#$%^-_(){} \'`'
symbols_list = []

for x in symbols:
    symbols_list.append(x)

def normalize(string):

    '''проводить транскипцію строки'''

    translite_str = string.translate(TRANS)
    for symbols in translite_str:
        if symbols in symbols_list:
            translite_str = translite_str.replace(symbols, '_')
        
    return translite_str

def rename_file(path):

    '''переіменовує файли та папки'''

    listdir = os.listdir(path)

    for cell in listdir:
        new_path = path + f"\{cell}"
        if os.path.isdir(new_path):
            rename_file(new_path)
        
        dirpath, filename = os.path.split(new_path)
        os.rename(new_path, dirpath + f"\{normalize(filename)}") 

#####################

IMAGES = ['.jpeg', '.png', '.jpg', '.svg']
DOCUMENTS = ['.doc', '.docx', '.txt', '.pdf','.xlsx', '.pptx']
AUDIO = ['.mp3','.ogg','.wav','.amr']
VIDEO = ['.avi', '.mp4', '.mov', '.mkv']
ARCHIVES = ['.zip','.gz','.tar']

def sort_file(path, my_dirs, PATH, result):

    '''створює нові папки; сортує файли по групам за їх рзширенням; видаляє пусті папки'''

    #створює нові папки
    try:
        os.mkdir(PATH + r'\images')
        os.mkdir(PATH + r'\documents')
        os.mkdir(PATH + r'\audio')
        os.mkdir(PATH + r'\video')
        os.mkdir(PATH + r'\archives')
        os.mkdir(PATH + r'\unknown')

    except FileExistsError:
        pass

    #сортує файли по групам за їх рзширенням
    listdir = os.listdir(path)
    listdir = list(set(listdir) - set(my_dirs))

    for cell in listdir:
        new_path = path + f"\{cell}"
        ext = os.path.splitext(cell)

        if ext[1] in DOCUMENTS:
            result['documents'].append(''.join(ext))
            destination = PATH + r'\documents'
            shutil.move(new_path, destination)

        elif ext[1] in AUDIO:
            result['audio'].append(''.join(ext))
            destination = PATH + r'\audio'
            shutil.move(new_path, destination)

        elif ext[1] in IMAGES:
            result['images'].append(''.join(ext))
            destination = PATH + r'\images'
            shutil.move(new_path, destination)
        
        elif ext[1] in VIDEO:
            result['video'].append(''.join(ext))
            destination = PATH + r'\video'
            shutil.move(new_path, destination)

        elif ext[1] in ARCHIVES:
            result['archives'].append(''.join(ext))
            destination = PATH + r'\archives'
            shutil.move(new_path, destination)
            
        
        elif os.path.isfile(new_path):
            dirpath, filename = os.path.split(new_path)
            result['unknown'].append(filename)
            destination = PATH + r'\unknown'
            shutil.move(new_path, destination)

        
        if os.path.isdir(new_path):
            sort_file(new_path, my_dirs, PATH, result)
    
    #видаляє пусті папки
    listdir = os.listdir(path)
    listdir = list(set(listdir) - set(my_dirs))
    for cell in listdir:
        new_path = path + f"\{cell}"
        shutil.rmtree(new_path)

#################

def unpack(path):

    '''розпаковує та видаляює всі архіви в папці archives'''
    
    listdir = os.listdir(path + r'\archives')
    for cell in listdir:
        archive_path = path + r'\archives' + f'\{cell}'
        base, ext = os.path.splitext(cell)
        archive_dir_path = path + r'\archives' + f'\{base}'
        if os.path.isfile(archive_path):
            shutil.unpack_archive(archive_path, archive_dir_path)
            os.remove(archive_path)

####################

def main():
    rename_file(path)
    sort_file(path, my_dirs, PATH, result)
    unpack(path)

    print('\nСписок файлів в кожній категорії:\n ')
    for k, v in result.items():
        str_result = f'{k}: '
        for it in v:
            str_result += f'{it}, '
        print(str_result)

    print('\nПерелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці:\n')
    for k, v in result.items():
        if k == 'unknown':
            print('\nПерелік всіх розширень, які скрипту невідомі.\n')
        str_result = f'{k}: '
        ass = []
        for it in v:
            base, ext = os.path.splitext(it)
            ass.append(ext)
            ass1 = set(ass)
        for x in ass1:
            str_result += f'{x}, '
        print(str_result)

if __name__ == '__main__':
    main()