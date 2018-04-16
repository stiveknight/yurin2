import json
import os
from sysfile import Sysfile
import properties


def dfs(path):
    if os.path.isfile(path):
        file = Sysfile(path, 0)
        file.serialization()
    elif os.path.isdir(path):
        if properties.path != path:
            file = Sysfile(path, 1)
            file.serialization()
        for item in os.listdir(path):
            dfs(path + '\\' + item)


def create_default_json(path):
    w = {}
    for name in path.split('\\')[::-1]:
        w = {name: {"isdir": 1, "subfiles": w}}
    with open("nastia.json", 'w') as file:
        file.write(json.dumps(w))


def main(path):
    # обход католга и дамп слепка каталога в файл
    # и возможно сравнение с предыдущим слепком
    create_default_json(path)
    dfs(path)


main(properties.path)
