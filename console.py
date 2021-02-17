#!/usr/bin/python3
"""Command interpreter for HBNB project"""
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

    intro = 'Welcome to the hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'EOF (CTRL + D) command to exit the program\n'
        print()
        return True

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
        # check if user didn´t type a class name
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        # check if class name exist
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

    # DRY = dont repeat yourself

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

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered, it would return the following:

        >   return self.onecmd(self.lastcmd)

        Further solution:

        >   pass

        """

        """if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')"""
        pass

    def postcmd(self, stop: bool, line: str) -> bool:
        return super().postcmd(stop, line)

    def precmd(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def postloop(self):
        """postloop docstring"""
        print()

# call the cmdloop() on the class HBNB (casted as a
# instance with "()"), it can also be done as follows
# HBNB_app = HBNBCommand()
# HBNB_app.cmdloop()
# in case you need the instance HBNB_app later in your programm
# magic method
# .cmdloop() ---> keeps the cmd opened


if __name__ == '__main__':
    HBNBCommand().cmdloop()
