import sys
from unittest import TestCase
from lib.development import BookFlight

class TestConstructor(TestCase):

    def test_title(self):
        book = BookFlight("test")

        self.assertIsInstance(book.title, str)

    def test_user_name(self):
        book = BookFlight("test")
        user_name = book.get_user_name()

        self.assertIsInstance(user_name, str)

    