# # 3. Scrieti un program care sa ceara utilizatorului sa introduca doua 
# numere, iar apoi sa afiseze suma lor. Daca utilizatorul introduce un 
# input invalid (de exemplu, un sir de caractere in loc de numere), 
# programul ar trebui sa afiseze un mesaj corespunzator de eroare.

def suma(a, b):
    """Calculate the sum of two numbers."""
    try:
        suma_res = int(a + b)
    except ValueError:
        print(f"Oops, try again with the correct input!")
    else:
        print(f"The sum of your numbers is: {suma_res}!")
    
a_in = input("Your first number is: ")
b_in = input("Your second number is: ")

suma(a_in, b_in)
