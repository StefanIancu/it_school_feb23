# Sa se afiseze topul elevilor. 


catalog = [
    ["Moise", [4, 5, 8]],
    ["Stefan", [8, 8, 10]],
    ["Nicusor", [4, 4, 6]]
]

podium=[]
catalog_sortat = sorted(catalog, reverse=True)

for elev in catalog:
    media_aritmetica = sum(elev[1]) / len(elev[1])
    print(elev[0], "are media ", media_aritmetica)
    podium.append(media_aritmetica)
    if media_aritmetica > 8.5:
        print(elev[0], "este premiant!")
    elif media_aritmetica < 5.0: 
        print(elev[0], "este corigent")
        print(elev[0], "ne vedem la toamna!")
print("Topul elevilor este: ", elev[1].sort)             #De aflat topul elevilor?

podium_sortat = sorted(podium)
print("Mediile, in ordine crescatoare, sunt:", podium_sortat)

media_clasa = sum(podium) / len(podium)

print("Media clasei este: ", media_clasa)
print("Cea mai mare medie este", max(podium))

if media_clasa <= 6.5:
    print("Fara vacanta anul asta!")

print(catalog_sortat)

