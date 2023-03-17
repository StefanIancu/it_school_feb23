# *args
#produsul tuturor argumentelor 

def n_product(*args):
    p = 1
    for i in args:
        p *= i
    return p 

print(n_product(1, 2, 3, 4, 5))

