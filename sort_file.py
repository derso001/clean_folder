import os
import shutil


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