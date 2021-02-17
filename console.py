#!/usr/bin/python3
"""module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class that inherits from cmd.Cmd"""
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
