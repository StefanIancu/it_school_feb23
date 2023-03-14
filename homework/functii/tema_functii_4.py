# 9. Managerul de la fabrica de cutii are nevoie de un program care calculeaza pretul
# cutiilor in functie de dimensiunea si grosimea lor. Pentru o cutie cu volumul de 1000 de litri
# de gorsime 1, pretul este de 25 de lei.
# Pentru gorosimile 2 si 3, pretul creste cu 10 respectiv 20 la suta.
# Scrieti o functie care primeste 4 parametrii:
# - inaltimea cutiei
# - latimea cutiei
# - lungimea cutiei
# - tipul de carton (1, 2 sau 3)
# Functia returneaza pretul.

def pret_cutie(inaltime, latime, lungime, tip_carton):
    pret_brut = inaltime * latime * lungime * 25
    if tip_carton == 1:
        return pret_brut
    if tip_carton == 2:
        return pret_brut * 1.1 
    if tip_carton == 3:
        return pret_brut * 1.2
    return None
    
inaltime_in = int(input("Inaltimea cutiei este: "))
latime_in = int(input("Latimea cutiei este: "))
lungime_in = int(input("Lungimea cutiei este: "))
tip_carton_in = int(input("Tipul cartonului este: "))
cantitate = int(input("Numarul de cutii dorit: "))

print(f"Pretul cutiei este de {pret_cutie(inaltime_in, latime_in, lungime_in, tip_carton_in)} RON.")

# 10. Scrieti o functie care genereaza o oferta de pret pentru managerul de la fabrica 
# de cutii. Functia trebuie sa aplice un discount de cantitate. Pentru fiecare 100 de cutii se
# aplica 1% reducere. Functia primeste toti parametrii necesari pentru calculul pretului cutiei si
# inca un parametru care reprezinta numarul de cutii.

def offer(inaltime, latime, lungime, tip, cantitate):
    pret_baza = pret_cutie(inaltime, latime, lungime, tip) 
    discount = cantitate // 100 
    pret_final = pret_baza * cantitate * (100 - discount / 100)
    return pret_final

print(f"Oferta personalizata este de {offer(inaltime_in, latime_in, lungime_in, tip_carton_in, cantitate):.2f}")



