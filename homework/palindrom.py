# 7. Scrie un program care citeste de la tastatura un nr. natural
# si verifica daca acesta este palindrom. 111 121 292 2992 33533


n = int(input("Alegeti numarul natural: "))

temp = n
reverse_num = 0

while n > 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n = n // 10

if temp == reverse_num:
    print("Este palindrom!")

else: 
    print("Nu este palindrom!")














