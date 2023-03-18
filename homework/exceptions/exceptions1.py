# 1. Scrieti un program care sa imparta doua numere intregi citite de la tastatura si sa afiseze catul si restul. 
# In cazul in care impartirea nu poate fi realizata (de exemplu, in cazul in care al doilea numar este 0), 
# programul ar trebui sa afiseze un mesaj corespunzator de eroare.


def divider(a, b):
    """Divide two numbers"""
    try:
        result = a / b 
    except ZeroDivisionError:
        print(f"Oops, looks like I am not able to do this!")
    else:
        print(f"Great, the result is {result}")


a_in = int(input("Choose your first number: "))
b_in = int(input("Choose your second number: "))

divider(a_in, b_in)


