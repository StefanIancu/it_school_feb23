# csv = comma separated values

import csv

#citire 
with open('salarii.csv') as fin:
    reader = csv.reader(fin.readlines())

for line in reader:
    #print(45 / 100 * int(line[-2]))
    print(f"Name: {line[0]} {line[1]}")

with open("salarii.csv") as fin:
    reader = csv.DictReader(fin.readlines(), delimiter="|")  #in cazul in care avem header si ne intereseaza sa returnam un dict

#scriere 

creeaza un csv cu nume prenume si salariu net 