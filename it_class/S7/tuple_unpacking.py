elev = ("Mihai", 8.7, 10)

print(elev[0])

# tuple unpacking

#nume_elev, nota_elev, _ = elev      #underscore pt o valoare care nu imi trebuie 

nume_elev, *others = elev       #*steluta pentru restul elementelor, vor fi grupate intr-o lista 

print(nume_elev)
print(others)

#print(nota_elev)

