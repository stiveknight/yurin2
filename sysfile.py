# import json
#
#
# class Sysfile:
#     def __init__(self, path, isdir):
#         self.name = self.get_name(path)
#         self.abspath = path
#         self.isdir = isdir
#         self.dir = path.split('\\')[:-1]
#         self.otnositelnie_path = ''
#         self.hash = 1
#
#     def is_folder(self):
#         return False
#
#     def get_name(self, path):
#         return path.split('\\')[-1]
#
#     def serialization(self):
#         with open("nastia.json", 'r') as file:
#             js = json.load(file)
#         js_to_dump = js
#         print(self.dir)
#         for name in self.dir:
#             js = js[name]['subfiles']
#         js[self.name] = {'isdir': 1, 'subfiles': {}}
#         with open('nastia.json', 'w') as file:
#             json.dump(js_to_dump, file)
