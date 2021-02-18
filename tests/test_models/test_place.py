#!/usr/bin/python3
import unittest
from models import place
from models.place import Place
import pep8


class TestPlace(unittest.TestCase):

    """TestPlace Class tests all the class """

    def test_pep8(self):
        """Check base model to be pep8 compliant"""
        fchecker = pep8.Checker("models/place.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_doc(self):
        """Check if class and methods are documented"""
        self.assertIsNotNone(place.__doc__)
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)
        self.assertIsNotNone(Place.__str__.__doc__)
        self.assertIsNotNone(Place.save.__doc__)
        self.assertIsNotNone(Place.to_dict.__doc__)

    def test_init(self):
        inst = Place()
