def pretul_cutiilor(inaltime, latime, lungime, tip_carton):
    pret_brut = inaltime * latime * lungime * 25
    if tip_carton == 2:
        return pret_brut * 1.1
    if tip_carton == 3:
        return pret_brut * 1.2 
    return pret_brut

print(f"Pretul cutiei tale este {pretul_cutiilor(1, 1, 1, 3)}")
    