import os


def current_folder():
    res = []
    for f in os.listdir('.'):
        dic = {}
        if os.path.isfile(f):
            dic['filename'] = f
            dic['type'] = 'File'
        elif os.path.isdir(f):
            dic['filename'] = f
            dic['type'] = 'Folder'
        res.append(dic)
    return res
