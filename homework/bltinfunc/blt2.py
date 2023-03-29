# 2. Sa se scrie o functie care primeste o lista de numere si 
# verifica daca exista cel putin un numar pozitiv. Functia trebuie sa returneze 
# True daca exista cel putin un numar pozitiv, si False altfel. Folositi functia any.


list = []

n = int(input("Length of the list: "))

for i in range(n):
    element = int(input("Your number: "))
    list.append(element)

def func_any(lista):
    return any(lista)

print(func_any(list))