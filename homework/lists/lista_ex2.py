# 2. Scrieti o functie care returneaza True daca lista primita ca param. este sortata,
# altfel returneaza False.

lista = []

for i in range(5):    
    lista.append(int(input("Numarul este: ")))

print("Your list is: ", lista)

if lista == sorted(lista):
    print("True, the list is sorted")
else:
    print("False, the list isn't sorted")



