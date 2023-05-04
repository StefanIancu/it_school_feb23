import time
from pathlib import Path

def fib_numb():
    a = 0
    b = 1

    while True:
        yield b
        a, b = b, a + b 

numb_gen = fib_numb()

# first_10_elements =[numb_gen.__next__() for i in range(10)]

script_path = Path(__file__)
new_folder_path = script_path.parent / "Fibonacci"

new_folder_path.mkdir(exist_ok=True, parents=True)


for i in numb_gen:
    file_name = i
    time.sleep(1)
    with open(new_folder_path / f"{file_name}.txt", "w") as fout:
        fout.write(str(i))
    if i == 233:
        print("Execution finished.")
        break





