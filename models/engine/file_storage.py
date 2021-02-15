#!/usr/bin/python3
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        n_obj = "{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )
        FileStorage.__objects[n_obj] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        try:
            f = open(FileStorage.__file_path, "r", encoding="utf-8")
            FileStorage.__objects = json.loads(f.read())
        except:
            return
        else:
            f.close()
