r1 = range(10) #de la default 0 la 9 
r2 = range(45, 91) #de la 45 la 90
r3 = range (20, 40, 2)  #de la 20 la 40 din doi in doi (start, stop, pas)
r4 = range (50, 25, -5) #DESCRESCATOR - pt ca are minus pasul de la 50 la 30...
r5 = range(3, 100, 3)


#suma multip de 5 din intervalul 0-1000:

counter = 0
r6 = range(5, 1000, 5)

for i in r6:
  
  counter += i

print(counter)
        


