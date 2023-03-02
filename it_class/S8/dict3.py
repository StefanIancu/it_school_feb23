catalog = {
    "Ana": 6.7,
    "Marius": 8.5,
    "Ion": 4.5
}

# valori = catalog.items()

# print(sorted(valori))    #sortare dupa cheie alfabetic

# for k, v in sorted(catalog.items()):
#     print(k, v)

#sortare dupa valori folosing functie

def extract(x):
    return x[1]


for k, v in sorted(catalog.items(), key=extract):
    print(k, v)


#sortare dupa valori cu lambda

for k, v in sorted(catalog.items(), key=lambda x: x[1]):
    print(k, v)



