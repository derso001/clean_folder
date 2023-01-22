import os

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