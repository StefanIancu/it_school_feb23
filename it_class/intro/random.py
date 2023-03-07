from random import randint

numar = randint(1, 99)

print("Incepe jocul!")

choice = int(input("Introduceti un numar intre 1 si 99: "))

while choice != numar:
    if choice < numar:
        print("+++")
    else:
        print("---")

print("Felicitari! Ati ghicit numarul!")
print("Numarul generat a fost ", numar)




