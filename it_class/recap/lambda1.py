def half_square(a):
    return a ** 2 / 2

# print(half_square(4))

l1 = [22, 2345, 66, 4234, 213123]
# l2 = list(map(half_square , l1))
l2 = list(map(lambda a : a ** 2 / 2, l1))
# l2 = [x ** 2 / 2 for x in l1]

#MAP  - apelezi o func pe fiecare elem dintr-o lista 

#sintaxa = lambda : 
#                  args, args1 <- : -> return value

# for i in l1:
#     l2.append(half_square(i))

print(l2)