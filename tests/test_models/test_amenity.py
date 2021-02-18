#!/usr/bin/python3
import unittest
from models import amenity
from models.amenity import Amenity
import pep8


class TestAmenity(unittest.TestCase):

    """TestAmenity Class tests all the class """
    # Parce listo, a hacer test a la lata

    # Este checkea el pep8
    def test_pep8(self):
        """Check base model to be pep8 compliant"""
        fchecker = pep8.Checker("models/amenity.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_doc(self):
        """Check if class and methods are documented"""
        self.assertIsNotNone(amenity.__doc__)
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)
        self.assertIsNotNone(Amenity.__str__.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)

    def test_init(self):
        inst = Amenity()
