#simple list comprehension
patrate_perfecte = [i * i for i in range(11)]
print(patrate_perfecte)

#list comprehension with if condition included 
sentence = "ground control to Major Tom"
vowels = [i for i in sentence if i in "aieou"]
print(vowels)

#replace negative prices using comprehension
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)

# #si aici comprehension-ul de mai sus detaliat intr-o functie 
# >>>def get_price(price):
#     return price if price > 0 else 0
# ...prices = [get_price(i) for i in original_prices]
# >>>prices
# >>>[1.25, 0, 10.22, 3.78, 0, 1.16]

#simple set comprehension - *items not in a particular order and no duplicates
sentence2 = "ground control to Major Tom"
vowels2 = {i for i in sentence if i in "aieou"}
print(vowels2)

print(f"Diferenta dintre lista {vowels} si set-ul {vowels2} este aceea ca \
      lista tine itemele ordonate si contine duplicate, in timp ce setul nu")

#dictionary comprehension - use a key first
squares = {i: i for i in range(10)}
print(squares)

#nested comprehension
cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temp = {city: [0 for _ in range(7)] for city in cities}
print(temp)

#matrix creation 
matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)

# A) flattening nested comprehension where "for" should be used - see below 
matrix = [     
    [0, 0, 0],
    [1, 1, 1],    
    [2, 2, 2],
 ]

flat = [num for row in matrix for num in row]
print(flat)

# B) the above example explained using "for"

flat1 = []
for row in matrix:
    for num in row:
        flat1.append(num)

print(flat1)

