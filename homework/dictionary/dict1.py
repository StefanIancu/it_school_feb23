# 1. Creați un dicționar care să conțină numele și vârsta a trei persoane.
# Apoi, iterați prin dicționar și afișați numele și vârsta fiecărei persoane.

familie = {
    "Stefan": 25, 
    "Andreea": 24, 
    "Gabriela": 52, 
    "Gabriel": 51
}

for k, v in familie.items():
    print(k + " are varsta " +str(v))

print("-" * 30)

# 2. Creați un dicționar cu numele și notele a trei studenți.
# Calculați media notelor și afișați-o alaturi de numele studentului.

catalog = {
    "Marian": [9, 9, 7],
    "Florentina": [6, 7, 9],
    "Nicu": [3, 4, 6]
}

for k, v in catalog.items():
    media_aritmetica = sum(v) / len(v)
    print(k, media_aritmetica)
    if media_aritmetica < 5.0:
        print("Elevul " + k + " este corigent!")

print("-" * 30)


# 3. Creați un dicționar cu numele și salariul a trei angajați.
# Afișați salariatul cu cel mai mare salariu.

salarii = {
    "Andreea": 5000, 
    "Florentina": 4000, 
    "Mihai": 3000
}

for k, v in salarii.items():
    print(k, v)

max_salariu = max(salarii.values())
max_value = max(salarii, key=salarii.get)

print("Angajatul cu cel mai mare salariu este: " + max_value)
print("Cel mai mare salariu este: " + str(max_salariu))

print("-" * 30)

#  4. Creați un dicționar cu numele și data de naștere a trei persoane.
# Adăugați o nouă persoană la dicționar și afișați numele și data de naștere a
# tuturor persoanelor.

zile_nastere = {
    "Andreea": {
        "Ziua": 9,
        "Luna": "August"
    },
    "Stefan": {
        "Ziua": 28, 
        "Luna": "Februarie"
    },
    "Marian": {
        "Ziua": 19, 
        "Luna": "Iunie"
    }
}

zile_nastere["Florentina"] ={
    "Ziua": 1, 
    "Luna": "Aprilie"
}


# for k, v in zile_nastere.items():
#     lista_luni= list(v.values())
#     for luna in lista_luni:
#         luna  == True
#     lista_zile = list(v.keys())
#     for zi in lista_zile:
#         zi == True
#     print(k + " este nascut in " + zi + " " + luna)

# print(lista_luni)
# print(lista_zile)

#lipseste ziua din rezolvare

print("-" *30)

# 5. Creați un dicționar cu numele și adresa a trei prieteni.
# Modificați adresa celui de-al doilea prieten și afișați dicționarul actualizat.

agenda = {
    "Dani": "Cehia, Praga",
    "Gabi": "Germania, Bremen",
    "Viorel": "Romania, Otopeni"
}

agenda["Gabi"] = "Romania, Bucuresti"

for k, v in agenda.items():
    print(k + " locuieste in " + v)

print("-" * 30)

# 6. Creați un dicționar cu numele și vârsta a trei persoane.
# Ștergeți persoana cu vârsta cea mai mică și afișați dicționarul actualizat.

nume_varsta = {
    "Marian": 51,
    "Floretina": 49, 
    "Gabriela": 27
}

del nume_varsta["Gabriela"]

for k, v in nume_varsta.items():
    print(k +" are " + str(v) + " ani.")

print("-" *30)


# 7. Creați un dicționar cu numele și ocupația a cinci persoane.
# Apoi, utilizați un buclă "for" pentru a itera prin dicționar și afișați numele
# și ocupația fiecărei persoane.

lista_ocupatii = {
    "Stefan": "Developer",
    "Marian": "Inginer", 
    "Andreea": "Educatoare",
    "Andrei": "Regizor",
    "Ileana": "Vanzatoare"
}

for k, v in lista_ocupatii.items():
    print(k + " are ocupatia de " + v)

print("-" *30)

# 8. Creați un dicționar cu numele și numărul de telefon a trei prieteni.
# Afișați numerele de telefon în ordine alfabetică a numelor.

numere_telefon = {
    "Mircea": "0771882933",
    "Zaharia": "032139122",
    "Andrei": "0722111888"
}

for k, v in sorted(numere_telefon.items()):
    print(k, v)

print("-" * 30)

# 9. Creați un dicționar cu numele și nota a cinci studenți.
# Afișați numele studentului cu cea mai mare notă.

nota_biologie = {
    "Anghel": 4,
    "Ionel": 2, 
    "Marta": 7, 
    "Paraschiv": 9, 
    "Claudia": 10
}

name = max(nota_biologie, key=nota_biologie.get)
print("Cea mai mare nota este: " + name + " " + str(max(nota_biologie.values())))

 
# The get() method returns the value for the specified key if the key is in the dictionary.

print("-" * 30)

# 10. Creați un dicționar cu numele și vârsta a patru persoane.
# Sortați dicționarul în funcție de vârstă și afișați numele și vârsta
# fiecărei persoane în ordine crescătoare de vârstă.

dict_varsta = {
    "Gabi": 52, 
    "Stefan": 25, 
    "Andreea": 12,
    "George": 73
}

for k, v in sorted(dict_varsta.items(), key=lambda x: x[1]):
    print(k, v)

print("-" * 30)

# print((lambda x, y : x*y)(5, 5))
#        #def nr arg=>return ecuatia=>argu

# lambda cu argumentele x si y returneaza expresia dorita (ex x + y), iar in paranteze urmeaza argumentele

# 11. Creați un dicționar cu numele și notele a patru studenți.
# Afișați numele și media fiecărui student în ordine descrescătoare a mediei.

note_istorie = {
    "Mariana": [9, 9, 7],
    "Florentin": [6, 7, 9],
    "Nina": [3, 4, 6],
    "Paul": [7, 5, 3]
}

for k, v in sorted(note_istorie.items()):
    medie = sum(v) / len(v)
    print(k, medie)

    