import sys
from unittest import TestCase
from unittest import mock
from nose.tools import *
from lib.development import BookFlight, WhereToGo, UTILS, PlaneTicket
import unittest
from unittest.mock import mock_open, patch

class TestConstructor(TestCase):

    def test_title(self):
        book = BookFlight("bookflight")

        self.assertIsInstance(book.title, str)

    # def test_user_yes(self):
    #     original_input = mock.builtins.input
    #     mock.builtins.input = lambda _: "yes"
    #     self.assertEqual(BookFlight.get_user_name(), "you entered yes")
    #     mock.builtins.input = original_input

# class TestWhere(TestCase):

#     def test_where_title(self):
#         where = WhereToGo("where")
#         self.assertIsInstance(where.title, str)

#     def test_list_destinations(self):
#         pass


# class TestMain(TestCase):
#     def test_get_dest(self):
#         m = mock_open(read_data='destinations.csv')
#         with patch("lib.development.WhereToGo", m) as mocked_open:
#             myclass_instace = WhereToGo("title")
#             version = myclass_instace.see_list_of_destinations()
#             content = "what"
#             self.assertEqual(version, content)
#             m.assert_called_with(f"{UTILS}/destinations.csv")

class TestTicket(TestCase):

    def test_title(self):
        ticket = PlaneTicket("test","TestTest",48,10,"test", "test", "test")
        self.assertIsInstance(ticket.title, str)