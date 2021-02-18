#!/usr/bin/python3
import unittest
from models import user
from models.user import User
import pep8


class TestUser(unittest.TestCase):

    """TestUser Class tests all the class """
    # Parce listo, a hacer test a la lata

    # Este checkea el pep8
    def test_pep8(self):
        """Check base model to be pep8 compliant"""
        fchecker = pep8.Checker("models/user.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_doc(self):
        """Check if class and methods are documented"""
        self.assertIsNotNone(user.__doc__)
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)

    def test_init(self):
        inst = User()
