from unittest import TestCase
from src.lib.atm import ATM
from datetime import datetime


class TestConstructor(TestCase):

    def test_attributes_values(self):
        """Test that the attributes get the correct value."""
        ing = ATM()

        self.assertIsInstance(ing.__service_mode, bool)
        self.assertIsInstance(ing.__pin, str)
        self.assertEqual(ing.__retry_counter, 0)

        for k in ing.__vault.keys():
            self.assertIn(k, [1, 5, 10, 20, 50, 100, 200, 500])


    def test_fill(self):
        