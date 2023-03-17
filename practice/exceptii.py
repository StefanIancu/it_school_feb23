list = [
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4]
]

for i in list:
    try:
        val = i[2]
    except IndexError:
        print(f"Index 2 not found in list {i}")
    else: 
        print(val)
    finally:
        print("I am going to print this after every iteration...")
    


