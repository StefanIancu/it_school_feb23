import time

def get_numbers():
    return [2, 3, 4, 5, 6, 7, 8, 44, 45, 35, 435]

x = get_numbers()
# print(x)

def rand_numb():
   a = 1
   
   while True: 
      yield a
      a += 1

numb_gen = rand_numb()


# try:
#     print(next(numb_gen))
#     print(next(numb_gen))
# except StopIteration:
#     print("End of generator!")


for i in numb_gen:
    time.sleep(1)
    print(i)
    if i == 5:
        print("END")