import os
import shutil
import sys
from normalize import rename_file
from sort_file import sort_file
from unpack import unpack

#python homework_1.py C:\Users\zdoro\Desktop\мотлох

arg = sys.argv[1]
PATH = f'{arg}'
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