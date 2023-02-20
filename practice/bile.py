#Intr-o cutie se află 300 de bile, numerotate cu numere începând de la unu, 
#din trei în trei. Toate bilele cărora le corespund numere pare sunt verzi. 
#Să se afle câte bile verzi sunt.


nr_bile = 300
nr_iteratie = 0 
nr_crt = 1
bile_verzi = 0

while nr_iteratie < nr_bile:
    nr_iteratie += 1 
    if nr_crt % 2 == 0:
        bile_verzi += 1
    nr_crt += 3

print(bile_verzi)
