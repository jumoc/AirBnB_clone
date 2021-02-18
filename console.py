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
        "Quit command to exit the program\n"
        return True

    def do_EOF(self, line):
        "EOF (CTRL + D) command to exit the program\n"
        print()
        return True

    def emptyline(self):
        """new line when not a command """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def search_instance(self, args):
        """Searches for an instance given a list of arguments"""
        n_dict = models.storage.all()
        for key, value in n_dict.items():
            if (value.to_dict()["id"] == args[1]) and\
                    (value.to_dict()["__class__"] == args[0]):
                return value
        return None

    def do_create(self, line):
        """Creates an instance of a class
            Usage: create [class name]\n"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instance = HBNBCommand.classes[args[0]]()
        print(instance.id)
        models.storage.save()

    def do_show(self, line):
        """Show an instance of a class given an id
            Usage: show [class name] [id]\n"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if not args[0] in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance = self.search_instance(args)
        if instance is not None:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an instance of a class given an id
            Usage: destroy [class name] [id]\n"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if not args[0] in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        n_dict = models.storage.all()
        for key, value in n_dict.items():
            if (value.to_dict()["id"] == args[1]) and\
                    (value.to_dict()["__class__"] == args[0]):
                n_dict.pop(key)
                models.storage.__objects = n_dict
                models.storage.save()
                return
        print("** no instance found **")

    def do_all(self, line):
        """Print all instances depending on the argument given
            Usage: all [class name]\n"""
        args = shlex.split(line)
        instances = []
        n_dict = models.storage.all()

        if len(args) > 0 and not args[0] in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        for key, value in n_dict.items():
            instance = None
            if len(args) == 0:
                instance = value
            elif args[0] == value.to_dict()["__class__"]:
                instance = value
            if instance is not None:
                instances.append(instance.__str__())
        print(instances)

    def do_update(self, line):
        """Updates or creates a value of a given instance\n"""
        args = shlex.split(line)
        # update <class name> <id> <attribute name> "<attribute value>"
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            instance = self.search_instance(args)
            if instance is None:
                print("** no instance found **")
            else:
                instance.__dict__[args[2]] = args[3]
                instance.save()

    def get_instances(self, name):
        n_dict = models.storage.all()
        instances = []

        for key, value in n_dict.items():
            instance = None
            if name is None:
                instance = value
            elif name == value.to_dict()["__class__"]:
                instance = value
            if instance is not None:
                instances.append(instance.__str__())
        return instances

    def default(self, line):
        args = line.split(".")
        if len(args) == 2:
            if args[1] == "all()":
                print(self.get_instances(args[0]))
            if args[1] == "count()":
                print(len(self.get_instances(args[0])))
            new_list = args[1].split("\"")
            if len(new_list) == 3:
                names = [args[0], new_list[1]]
                instance = self.search_instance(names)
                print(instance) if instance\
                    else print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
