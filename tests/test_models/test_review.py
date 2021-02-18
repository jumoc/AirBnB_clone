#!/usr/bin/python3
import unittest
from models import review
from models.review import Review
import pep8


class TestReview(unittest.TestCase):

    """TestReview Class tests all the class """

    def test_pep8(self):
        """Check base model to be pep8 compliant"""
        fchecker = pep8.Checker("models/review.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_doc(self):
        """Check if class and methods are documented"""
        self.assertIsNotNone(review.__doc__)
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)
        self.assertIsNotNone(Review.__str__.__doc__)
        self.assertIsNotNone(Review.save.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)

    def test_init(self):
        inst = Review()
