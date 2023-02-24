# 1. Scrieti o functie care returneaza reversul unei liste. Lista primita ca parametru nu 
# trebuie modificata.

lista = []

for element in range(5):
    lista.append(int(input("Numarul este: ")))



lista_1 = lista.copy()
lista_1.reverse()


print(lista)
print(lista_1)



