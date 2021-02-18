#!/usr/bin/python3
import unittest
from models import state
from models.state import State
import pep8


class TestState(unittest.TestCase):

    """TestState Class tests all the class """

    def test_pep8(self):
        """Check base model to be pep8 compliant"""
        fchecker = pep8.Checker("models/state.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_doc(self):
        """Check if class and methods are documented"""
        self.assertIsNotNone(state.__doc__)
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)
        self.assertIsNotNone(State.__str__.__doc__)
        self.assertIsNotNone(State.save.__doc__)
        self.assertIsNotNone(State.to_dict.__doc__)

    def test_init(self):
        inst = State()
