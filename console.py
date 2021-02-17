#!/usr/bin/python3
"""module"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """class that inherits from cmd.Cmd"""
    classes = {
        "BaseModel": BaseModel, "User": User,
        "State": State, "City": City, "Amenity": Amenity,
        "Review": Review, "Place": Place
    }
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'EOF (CTRL + D) command to exit the program\n'
        print()
        return True

    def emptyline(self):
        """new line when not a command """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
