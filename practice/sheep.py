def count_sheep(n):
    # n = int(input("Count your sheep... "))
    prag = 0 
    while prag < n:
        prag += 1
        return f"{prag} sheep..."
        


# print(count_sheep(3))




text = "double backed words"

def reverse_words(txt):
    return txt[::-1]


print(reverse_words(text))


import random

random.randint