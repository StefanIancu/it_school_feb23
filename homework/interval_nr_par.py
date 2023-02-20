# 2. Scrieti un program care afiseaza numerele impare in intervalul [0, 1000]

r1 = range(1, 1001)

for i in r1:
    if i % 2 != 0:
        print(i)
        