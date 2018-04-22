import json
import os
import hashlib
import properties


def md5(path):
    try:
        hash_md5 = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except PermissionError:
        return 0


class Sysfile:
    def __init__(self, path):
        self.name = self.get_name(path)
        self.abspath = path
        if os.path.isdir(path):
            self.isdir = 1
        else:
            self.isdir = 0
        self.dir = path.split('\\')[:-1]
        #self.otnositelnie_path = ''
        self.hash = md5(path)
        self.size = os.path.getsize(path)
        self.mod = os.path.getmtime(path)
        self.creation = os.path.getctime(path)
        self.open = os.path.getatime(path)


    def is_folder(self):
        return False

    def get_name(self, path):
        return path.split('\\')[-1]

    def comp(self, other):
        if self.hash == other['hash'] and self.size == other['f_size'] and self.mod == other['last_modification'] and self.creation == other['creation'] and self.open == other['last_open']:
            return True
        return False

    def serialization(self):
        # with open("nastia.json", 'r') as file:
        #     js = json.load(file)

        jss = properties.js
        # print(self.dir)
        for name in self.dir:
            jss = jss[name]['subfiles']
        jss[self.name] = {'isdir': self.isdir, 'f_size': self.size, 'hash': self.hash, 'last_modification': self.mod, 'creation': self.creation, 'last_open': self.open, 'subfiles': {}}
        # with open('nastia.json', 'w') as file:
        #     json.dump(js_to_dump, file)
