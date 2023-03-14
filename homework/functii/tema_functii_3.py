# 4. Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
# un singur agument reprezentand muchia cubului in metri.

def volum_cub(muchie):
    return muchie ** 3 

# muchie_in = int(input("Muchia cubului este: "))
# print(f"Volumul cubul in litri este {volum_cub(muchie_in)}")


# 5. Scrieti o functie care returneaza volumul unui cilintru in litri,
# Aceasta va primi doua argumente reprezentand inaltimea si raza bazei in metri.

def volum_cilindru(raza_baza, inaltime):
    return 3.14 * raza_baza ** 2 * inaltime 
   

# raza_baza_in = int(input("Raza bazei este: "))
# inaltime_in = int(input("Inaltimea este: "))

# print(f"Volumul cilindrului in litri este {volum_cilindru(raza_baza_in, inaltime_in)}")


# 6. Scrie o functie care converteste litrii in metri cubi.

def converter(litri):
    """Converts litres to cubic meters"""
    return litri * 0.001

# litri_in = int(input("How many liters: "))

# print(f"That means {converter(litri_in)} cubic meters!")


# 7. Foloseste functiile de la pct. 4-6 pentru a calcula cate cuburi cu muchia de 18 metri
# sunt necesare pentru a umple un cilindru cu raza bazei de 20 m si inaltimea de 55 m.
# - Printeaza volumul cubului in metri cubi #### Volumul cubului: 20 m^3
# - Printeaza volumul cilindrului in metri cubi.
# - Printeaza rezultatul de la pct. 7
# - Toate valorile printate vor fi insotite de mesaje descriptive.


print(f"Volumul cubului in metri cubi este {volum_cub(18)}")
print(f"Volumul cilindrului in metri cubi este {volum_cilindru(20, 55)}")
print(f"Numarul de cuburi necesare pentru a umple cilindrul este {volum_cilindru(20, 55) / volum_cub(18)}")