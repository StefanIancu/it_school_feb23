import sys
from unittest import TestCase
from unittest.mock import Mock
from nose.tools import *
from lib.development import BookFlight, WhereToGo, UTILS, PlaneTicket
from unittest.mock import mock_open, patch

data = Mock()

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

req = Mock()
class GetName(TestCase):

    def get_name(self):
        answer = Mock()
        answer.return_value = 10
        return answer


    def test_user_name(self): 
        req.side_effect = self.get_name()
        assert BookFlight.get_user_name(self) is str