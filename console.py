#!/usr/bin/python3
"""module"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    classes = {"BaseModel": BaseModel, "User": User}
    """class that inherits from cmd.Cmd

    .cmdloop()          ---> keeps the cmd opened
    it requires its positional argument self:
    Cmd.cmdloop() instead of Cmd.cmdloop()

    """
    intro = 'Welcome to the hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None
    """How to create commands?
    create a method inherited from cmd.Cmd

    """

    """command needs two arguments"""

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'EOF (CTRL + D) command to exit the program\n'
        print()
        return True

    def search_instance(self, args):
        n_dict = storage.all().copy()
        for key in n_dict:
            if (n_dict[key]["id"] == args[1]) and (n_dict[key]["__class__"] == args[0]):
                instance = HBNBCommand.classes[n_dict[key]["__class__"]](**n_dict[key])
                return instance
        return None

    def do_create(self, line):
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
        storage.save()
        print(instance.id)

    def do_show(self, line):
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

        n_dict = storage.all()
        for key in n_dict:
            if (n_dict[key]["id"] == args[1]) and (n_dict[key]["__class__"] == args[0]):
                n_dict.pop(key)
                storage.__objects = n_dict
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, line):
        args = shlex.split(line)
        instances = []
        n_dict = storage.all()

        if len(args) > 0 and not args[0] in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        for i in n_dict:
            instance = None
            if len(args) == 0:
                instance = HBNBCommand.classes[n_dict[i]["__class__"]](**n_dict[i])
            elif args[0] == n_dict[i]["__class__"]:
                instance = HBNBCommand.classes[n_dict[i]["__class__"]](**n_dict[i])
            if instance is not None:
                instances.append(instance.__str__())
        print(instances)

    def do_update(self, line):
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
                #¡Castear el tipo de objeto a su type corresponiente!
                instance.__dict__[args[2]] = args[3]
                instance.save()

"""call the cmdloop() on the class HBNB (casted as a
instance with "()"), it can also be done as follows

HBNB_app = HBNBCommand()
HBNB_app.cmdloop()

in case you need the instance HBNB_app later in your programm

"""
"""magic method"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
