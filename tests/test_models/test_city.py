#!/usr/bin/python3
import unittest
from models import city
from models.city import City
import pep8


class TestCity(unittest.TestCase):

    """TestCity Class tests all the class """

    def test_pep8(self):
        """Check base model to be pep8 compliant"""
        fchecker = pep8.Checker("models/city.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_doc(self):
        """Check if class and methods are documented"""
        self.assertIsNotNone(city.__doc__)
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)
        self.assertIsNotNone(City.__str__.__doc__)
        self.assertIsNotNone(City.save.__doc__)
        self.assertIsNotNone(City.to_dict.__doc__)

    def test_init(self):
        inst = City()
