# 1. Scrieti o functie care verifica daca unu nr este par.
# Daca este par returneaza True, altfel False. Functia are un singur argument.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False 
    

number = int(input("Numarul ales este: "))
print(f"Numarul ales de tine este: {is_even(number)}")

# 2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
# [0, 50] si in intervalul [2000, 2100].

for i in range(0, 51):
    if is_even(i) == False:
        print(i)

for i in range(2000, 2101):
    if is_even(i) == False:
        print(i)