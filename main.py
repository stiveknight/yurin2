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
    for name in path.split('\\')[::-1]:
        w = {name: {"isdir": 1, "f_size": 0, "hash": 0, "last_modification": 0, "creation": 0, "last_open": 0,
                    "subfiles": w}}
    with open("nastia.json", 'w') as file:
        file.write(json.dumps(w))


def compare(path):
    if os.path.isfile(path):
        pass
        # file = Sysfile(path, 0)
        # file.serialization()

    elif os.path.isdir(path):
        on_disk = os.listdir(path)
        with open('nastia.json', 'r') as file:
            js = json.load(file)
        for name in path.split('\\'):
            js = js[name]['subfiles']
        on_dump = js

        for name in on_disk:
            if not name in on_dump:
                print('Появился новый файл: ' + path + '\\' + name)
            else:
                s = Sysfile(path + '\\' + name)
                if not s.comp(on_dump[name]):
                    print('Файл был изменен: ' + path + '\\' + name)
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
    if input() == '1':
        create_default_json(path)
        open_file()
        dfs(path)
        close_file()
    else:
        compare(path)


main(properties.path)
