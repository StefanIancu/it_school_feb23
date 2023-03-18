# 2. Scrieti un program care sa ceara utilizatorului sa introduca un numar intreg, 
# iar apoi sa afiseze acel numar ridicat la puterea a doua. Daca utilizatorul 
# introduce un input invalid (de exemplu, un numar cu virgula), programul ar 
# trebui sa afiseze un mesaj corespunzator de eroare.

def square(a):
    """Calculate the square number of an integer."""
    try:
        square = int(a) ** 2
    except ValueError:
        return f"Oops, looks like you used a float or str. Try again with an integer."
    else: 
        return f"The square is: {square}"
    
    
a_in = input("Your integer is: ")
print(square(a_in))


# def true_int(x_in):
#     """Return T or F if the number is an int."""
#     if x_in != int:
#         return True
#     else:
#         return False
    

# x_in = input("Choose your integer: ")

# print(true_int(x_in))

# print(type(x_in))


# print(isinstance(1.5, float))



