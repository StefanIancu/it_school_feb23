list = [3, 5]


# def multiply_item(list):
#     result = 1
#     for i in list:
#         result *= i
#     return result


# print(multiply_item(list))

def square(list):
    result = 1
    for i in list:
        result = i ** i
    return result


print(square(list))