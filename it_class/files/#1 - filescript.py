from pathlib import Path

script_path = Path(__file__)
print(f"The path of this script is: {script_path}")

start_folder_path = script_path.parent / "data"

file_name = "1.txt"

start_folder_path.mkdir(exist_ok=True, parents=True)

with open(start_folder_path / file_name, "w") as fout:
    name = input("Hello, your name is? ")
    fout.write(name)

print("Execution done.")






