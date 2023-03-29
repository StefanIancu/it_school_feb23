from random import randint

print(f"Password Generator v1.0")

get_user_length = int(input("Password length: "))
get_user_use_digits = str(input("Use digits? [y/n] "))
get_user_use_symbols = str(input("Use symbols? [y/n] "))

def get_bool(x):
    """Returns True or False regarding user's input."""
    if x == "y" or x == "Y":
        return True
    else:
        return False 


ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random_digits = randint(0, 10)

lower_letters = [ord(i) for i in ascii_lowercase]
upper_letters = [ord(i) for i in ascii_uppercase]


def pass_gen(l, d, s):
    """Generate a password based on user's preference."""
    l = get_user_length
    d = get_user_use_digits
    s = get_user_use_symbols
    
