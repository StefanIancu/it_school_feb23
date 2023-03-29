# 1. Sa se scrie o functie care primeste o lista de numere si verifica 
# daca toate numerele sunt pozitive. Functia trebuie sa returneze True daca 
# toate numerele sunt pozitive, si False altfel. Folositi functia all.


list = [1, 5, 3]


def func_all(lista):
    return all(lista)
        
print(func_all(list))


