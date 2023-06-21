def binary(int: int):
    # return f"{int} in binary is {str(bin(int))[2:]}."
    return str(bin(int))[2:]

print(binary(2023))
print(binary(25))

first = int(binary(2023))
second = int(binary(25))

print(f"{binary(25)}/{binary(2023)}")
