#!/usr/bin/python3
"""module"""
import cmd


class HBNBCommand(cmd.Cmd):
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


"""call the cmdloop() on the class HBNB (casted as a
instance with "()"), it can also be done as follows

HBNB_app = HBNBCommand()
HBNB_app.cmdloop()

in case you need the instance HBNB_app later in your programm

"""
"""magic method"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
