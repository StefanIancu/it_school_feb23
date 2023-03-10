# 1. Creati un program care sa afiseze numele si prenumele vostru intr-un string folosind .format()

myself = {
    "first_name": "Stefan",
    "last_name": "Iancu",
    "age": 25,
    "occupation": "programmer"
}

MYSELF_TEMPLATE = "Subsemnatul prenume {} nume {} are varsta de {} ani si de profesie este {}."

# print(MYSELF_TEMPLATE.format(myself["first_name"], myself["last_name"], myself["age"], myself["occupation"]))

# print("*" *30)

#2. Creati un program care sa ceara utilizatorului numele si varsta, si sa afiseze un mesaj de salut personalizat.

# user_name = input("Name: ")
# user_age = input("Age: ")

USER_TEMPLATE = "Salut {}, in varsta de {} ani, ne bucuram ca ai revenit!"

# print(USER_TEMPLATE.format(user_name, user_age))

# 3. Creeaza o lista de cumparaturi cu cateva elemente in ea. (lista de stringuri).
# Creeaza un string formatat pentru a afisa ceva asemanator cu : Azi trebuie sa cumperi: mere, pere, struguri.

lista_cumparaturi = [
    "ciuperci",
    "cascaval",
    "porumb",
    "ceapa"
]

GROCERY_TEMPLATE = "Astazi va trebui sa cumpar {},{},{}."

# for aliment in lista_cumparaturi:
#     print(GROCERY_TEMPLATE.format(aliment))

# print(GROCERY_TEMPLATE.format(lista_cumparaturi[0], lista_cumparaturi[1], lista_cumparaturi[2], lista_cumparaturi[3]))

# 4. Creati un program care sa afiseze
    
#     $
#    ***
#   *****
#  *******
# *********

# print("{:^10}".format("$"))
# print("{:^10}".format("***"))
# print("{:^10}".format("*****"))
# print("{:^10}".format("*******"))
# print("{:^10}".format("*********"))

# print("{:^10}".format(n * "$"))

n = -1

while n <= 7: 
    n += 2
    print("{:^10}".format(n * "*"))
