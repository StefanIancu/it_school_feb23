a = int(input("Numarul pozitiv din trei cifre este: "))

if a < 100 or a >999:
    print("Eroare")
elif a % 10 >=5:
    print