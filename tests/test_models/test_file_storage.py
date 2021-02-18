#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
import pep8


class TestBaseModel(unittest.TestCase):

    def test_pep8(self):
        """Check base model to be pep8 compliant"""
        fchecker = pep8.Checker("models/engine/file_storage.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)