# 4. Scrieti un program care sa ceara utilizatorului sa introduca o lista de 
# numere intregi separate prin virgula, iar apoi sa afiseze suma lor. In cazul 
# in care inputul utilizatorului este invalid, programul ar trebui sa afiseze 
# un mesaj corespunzator de eroare.

def suma_numere(a, *args):
    """Calculate the sum of multiple input numbers"""
    try:
        produs = int(a + args)
    except ValueError:
        print("Ooops, looks like your input is invalid! Try again!")
    else: 
        print(produs)

lista_numere = []

n = int(input("Enter number of elements: "))

for i in range(0, n):
     element = int(input())
     lista_numere.append(element)

print(lista_numere)

a_in = input("First number is: ")

suma_numere(a_in, lista_numere)
     

