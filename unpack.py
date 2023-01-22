import os
import shutil

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