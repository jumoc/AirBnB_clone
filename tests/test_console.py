#!/usr/bin/python3
"""module"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class testCommand(unittest.TestCase):
    """Command test"""

    def test_help_quit(self):
        """test for quit command"""
        message = "Quit command to exit the program\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        stdo = f.getvalue()
        self.assertEqual(message, stdo)

    def test_help_EOF(self):
        """test for EOF [CTRL + D] command"""
        message = "EOF (CTRL + D) command to exit the program\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        stdo = f.getvalue()
        self.assertEqual(message, stdo)


if __name__ == "__main__":
    unittest.main()
