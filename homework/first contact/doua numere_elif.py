a = int(input("Numarul a este: "))
b = int(input("Numarul b este: "))


if a > b:
    ab1 = str(a - b)
    print("A minus B este: " + ab1)
    ab11 = str(a + b)
    print("A plus B este: " + ab11)

elif a == b:
    ab2 = str(a * (b * 2))
    print("A la puterea B este: " + ab2)


else: 
    c = str(a + b)
    print("Suma lor este: " + c)

