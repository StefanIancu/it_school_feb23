from unittest import TestCase
from src.lib.atm import Card
from datetime import datetime

class TestConstructor(TestCase):

    def test_attributes_values(self):
        """Test that the attributes are generated correctly."""
        card = Card("test", "0837")

        self.assertIsInstance(card.number, str)
        self.assertEqual(len(card.number), 8)
        
        self.assertIsInstance(card.expire_date, datetime)



class TestGetBalance(TestCase):

    def test_get_balance(self):
        """Test that the method returns an integer value 0."""
        card = Card("test", "0837") 
        #nu am inteles linia de mai sus. am creat un obiect 
        #de care sa ma folosesc mai jos pt a accesa atributele? 

        self.assertIsInstance(card.__balance, int)
        self.assertEqual(card.__balance, 0)



class TestAddMoney(TestCase):

    def test_add_money(self):
        """Test that the method returns updated balance."""
        card = Card("Ionel", "2111")
        value = 0

        self.assertIsInstance(card.__balance, int)
        self.assertGreater(value, 0)
        #am incercat sa testez daca valoarea introdusa e mai mare decat 0, 
        #altfel n-ar fi posibil sa alimentezi pe minus



class TestCheckPin(TestCase):

    def test_check_pin(self):
        """Test that the entered pin is equal to the actual pin."""
        card = Card("Marian", "6078")
        pin = card.check_pin   #???

        self.assertEqual(pin, card.__pin)
        

class TestWithdraw(TestCase):

    def test_withdraw(self):
        """Test that the withdraw amount is less or equal with the balance."""
        card = Card("John", "7777")
        withdraw = card.withdraw

        self.assertLessEqual(withdraw, card.__balance)
        self.assertIsInstance(card.__balance, int)



