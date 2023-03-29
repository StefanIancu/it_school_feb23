# 4. Sa se scrie o functie care primeste doua liste de numere si returneaza 
# o lista care contine suma elementelor de pe aceleasi pozitii. Folositi functia zip.

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

def suma_elem(lista1, lista2):
    """Calculate the sum of each elements on the same position from two lists"""
    lista_rez = zip(lista1, lista2)
    lista_rez = [sum(i) for i in lista_rez]
    return lista_rez

print(f"Suma elementelor din cele doua liste este: {suma_elem(list1, list2)}.")

