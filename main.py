import json
import os
from sysfile2 import Sysfile
import properties


def open_file():
    with open("nastia.json", 'r') as file:
        properties.js = json.load(file)


def close_file():
    with open('nastia.json', 'w') as file:
        json.dump(properties.js, file)


def dfs(path):
    if os.path.isfile(path):
        file = Sysfile(path)
        file.serialization()
    elif os.path.isdir(path):
        if properties.path != path:
            file = Sysfile(path)
            file.serialization()
        for item in os.listdir(path):
            try:
                dfs(path + '\\' + item)
            except:
                continue


def create_default_json(path):
    w = {}
    ww = path.split('\\')
    for idx, name in enumerate(path.split('\\')[::-1]):
        p = []
        for i in range(len(ww) - idx):
            p.append(ww[i])
        for idx in range(len(p)):
            if len(p) == 1:
                p[idx] += '\\'
        n_path = '\\'.join(map(str, p))
        s = Sysfile(n_path)
        w = {name: {"isdir": s.isdir, "f_size": s.size, "hash": s.hash, "last_modification": s.mod, "creation": s.creation, "last_open": s.open,
                    "subfiles": w}}
    with open("nastia.json", 'w') as file:
        file.write(json.dumps(w))


def compare(path):
    if os.path.isfile(path):
        pass
    elif os.path.isdir(path):
        on_disk = []
        try:
            on_disk = os.listdir(path)
        except PermissionError:
            print("Ошибка доступа к {} ".format(path))
            return
        js = js_c
        for name in path.split('\\'):
            js = js[name]['subfiles']
        on_dump = js

        for name in on_disk:
            if not name in on_dump:
                print('Появился новый файл: ' + path + '\\' + name)
            else:
                s = Sysfile(path + '\\' + name)
                s.comp(on_dump[name])
                # print('Файл был изменен: ' + path + '\\' + name)
                try:
                    compare(path + '\\' + name)
                except:
                    continue

        for name in on_dump:
            if not name in on_disk:
                print('Был удален файл: ' + path + '\\' + name)


def main(path):
    # обход католга и дамп слепка каталога в файл
    # и возможно сравнение с предыдущим слепком
    if input('Режим создания слепка [y/n]') == 'y':
        create_default_json(path)
        open_file()
        dfs(path)
        close_file()
    else:
        compare(properties.path_for_compare)


with open('nastia.json', 'r') as file:
    js_c = json.load(file)

main(properties.path)
