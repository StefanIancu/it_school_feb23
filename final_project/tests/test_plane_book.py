import sys
from unittest import TestCase
from lib.development import BookFlight

class TestConstructor(TestCase):

    def test_title(self):
        book = BookFlight("Test")

        self.assertIsInstance(book.__title, str)

