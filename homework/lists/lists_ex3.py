# Scrieti o functie care primeste doua liste ca parametri. Listele contin numere intregi.
# Fct. returneaza o singura lista formata din inmultirea dupa cum urmeaza: primul elem. din prima 
# lista X primul elem. din a 2-a lista .... etc.
# [1, 2, 3]
# [3, 4, 6]
# => [3, 8, 18]


lista1 = [1, 3, 5]
lista2 = [4, 6, 8]
rezultat = []

# for element in lista1:
#     rezultat.append((element * lista2[0]))

# print(rezultat)
    

for i1, i2 in zip(lista1, lista2):
    rezultat.append(i1*i2)

print(rezultat)

print(type(rezultat))