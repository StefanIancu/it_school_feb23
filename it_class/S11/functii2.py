def is_even(number):
    # scop local
    if number % 2 == 0:
        return True
    else:
        return False
    
for i in range(0, 51):
    if not is_even(i):
        print(i)


