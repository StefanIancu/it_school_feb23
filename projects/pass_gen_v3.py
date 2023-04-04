# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#remaining tasks:
#    1. check exceptions and errors !!!
#    2. improve the input
#    3. reverse the inputs when calling the pass_gen func
#       -eg firstly should appear the length question. 
#    4. final password shouldn't have duplicates

import random
from string import ascii_letters as alphabet
from string import digits 
from string import punctuation as symbols

all_characters = alphabet + digits + symbols
without_digits = alphabet + symbols
without_symbols = alphabet + digits



def get_user_length():
    """Gets the user wanted password length."""
    try:
        user_length = int(input("Password length: "))
    except ValueError:
        print("Sorry, wrong input. Need an int.")
    else: 
        return user_length
    
def get_user_digits():
    """Gets the user's preference for using digits."""
    try: 
        user_digits = input("Use digits? [y/n]")
    except ValueError:
        print("Sorry, need a yes or no.")
    else:
        if user_digits == "y":
            return True
        elif user_digits == "Y":
            return True
        else:
            return False
        
def get_user_symbols():
    """Gets the user's preference for using symbols."""
    try: 
        user_symbols = input("Use symbols? [y/n]")
    except ValueError:
        print("Sorry, need a yes or no.")
    else:
        if user_symbols == "y":
            return True
        elif user_symbols == "Y":
            return True
        else:
            return False
    
def generate_digitless_password():
    """Returns a digitless password."""
    for i in range(get_user_length()):
        print(random.choice(without_digits), end="")
        
def generate_symbless_password():
    """Returns a password without symbols."""
    for i in range(get_user_length()):
        print(random.choice(without_symbols), end="")
    
    
def generate_alphabetical_password():
    """Returns a password containing just letters."""
    for i in range(get_user_length()):
        print(random.choice(alphabet), end="")
    
    
def generate_full_password():
    """Returns a password with all characters."""
    for i in range(get_user_length()):
        print(random.choice(all_characters), end="")
        
        
    
def pass_gen():
    """Returns the final password for the user based on their preferences."""
    if get_user_digits():
        if get_user_symbols():
            generate_full_password()
        else:
            generate_symbless_password()
    else:
        if get_user_symbols():
            generate_digitless_password()
        else: 
            generate_alphabetical_password()


pass_gen()

                        
            
            



