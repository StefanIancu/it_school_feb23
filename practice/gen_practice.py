import time

def num_gen():
    a = 10

    while True:
        yield a 
        a -= 1

generator = num_gen()

for i in generator:
    time.sleep(1)
    print(i)
    if i == 1:
        print("START RACE!")
        break

