import string
import random

print(f"Password Generator v1.0")

# get_user_length = int(input("Password length: "))
# get_user_use_digits = str(input("Use digits? [y/n] "))
# get_user_use_symbols = str(input("Use symbols? [y/n] "))

def get_bool(x):
    """Returns True or False regarding user's input."""
    if x == "y" or x == "Y":
        return True
    else:
        return False 


letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols
without_digits = letters + symbols
without_symbols = letters + digits 


# for i in range(get_user_length):
    # if get_bool(get_user_use_digits) and get_bool(get_user_use_symbols):
    #     print(f"Your password is: {random.choice(all_characters)}")
    # elif get_bool(get_user_use_digits) and not get_bool(get_user_use_symbols):
    #     print(f"Your password is: {random.choice(without_symbols)}")
    # elif not get_bool(get_user_use_digits) and get_bool(get_user_use_symbols):
    #     print(f"Your password is: {random.choice(without_digits)}")

user_length = int(input("Pass:"))
user_digits = str(input("Digits? [y/n]"))
user_symbols = str(input("Symbols? [y/n]"))

def get_user_length():
    """Gets the user's wanted password length."""
    try:
        int(input("Password length: "))
    except ValueError:
        print("Wrong input. Please try again.")

def get_user_digits():
    """Gets the user's preference for using digits."""
    try:
       raspuns = input("Use digits? [y/n] ")
    except ValueError:
        print("Wrong input. I need a string.")
    else:
        if raspuns == "y" or "Y":
            return True

def get_user_symbols():
    """Gets the user's preference for using symbols."""
    try:
        input("Use symbols? [y/n]")
    except ValueError:
        print("Wrong input. I need a string.")

def generate_a_password():
    """Generates a password based on user's preferences."""
    return random.choice(all_characters)
    
def generate_a_digitless_password():
    return random.choice(without_digits)

def generate_a_symbless_password():
    return random.choice(without_symbols)



for i in range(user_length):
    if get_bool(user_digits) and get_bool(user_symbols):
        print(generate_a_password(), end="")
    if get_bool(user_digits) and not get_bool(user_symbols):
        print(generate_a_symbless_password(), end="")
    if get_bool(user_symbols) and not get_bool(user_digits):
        print(generate_a_digitless_password(), end="")


