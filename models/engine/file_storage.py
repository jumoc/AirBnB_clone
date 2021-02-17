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
        FileStorage.__objects[n_obj] = obj

    def save(self):
        """ send object to JSON """

        new_dict = {}
        for element in FileStorage.__objects:
            obj = FileStorage.__objects[element]
            obj_dict = obj.to_dict()
            new_dict[element] = obj_dict
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(new_dict))


    def reload(self):
        try:
            f = open(FileStorage.__file_path, "r", encoding="utf-8")
            FileStorage.__objects = json.loads(f.read())
        except:
            return
        else:
            f.close()
