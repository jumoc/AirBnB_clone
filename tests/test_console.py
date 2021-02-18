#!/usr/bin/python3
"""module"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class testCommand(unittest.TestCase):
    """Command test"""

    def test_quit(self):
        """test for quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        stdo = f.getvalue()
        self.assertEqual(stdo, "")

    def test_help_quit(self):
        """test for help quit command"""
        message = "Quit command to exit the program\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        stdo = f.getvalue()
        self.assertEqual(stdo, message)

    def test_EOF(self):
        """test for EOF (CTRL + D) command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        stdo = f.getvalue()
        self.assertEqual(stdo, "\n")

    def test_help_EOF(self):
        """test for help quit command"""
        message = "EOF (CTRL + D) command to exit the program\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        stdo = f.getvalue()
        self.assertEqual(stdo, message)


if __name__ == "__main__":
    unittest.main()
