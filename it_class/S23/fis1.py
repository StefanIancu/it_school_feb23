# /Users/stefantraianiancu/Desktop/it_school/it_class/S22/atm_project/tests/test_atm_card.py   = absolute path

# it_class/S22/atm_project/tests/test_atm_card.py = relative path

from pathlib import Path
from datetime import datetime

working_dir = Path('.') #current working directoy / pwd

print(working_dir)
# print(type(working_dir))

print(f"Current working directory: {working_dir.absolute()}")

script_path = Path(__file__)
print(f"Script path: {script_path}")

print(f"Script parent directory: {script_path.parent}")  #.parent se poate folosi de mai multe ori in continuare

print(f"Does {script_path} exists? {script_path.exists()}")

# /Users/stefantraianiancu/Desktop/it_school/it_class/S23/program_data/start_time
start_time_path = script_path.parent / "program_data" / "start_time"

print(start_time_path)

# if not start_time_path.parent.exists():
#     start_time_path.parent.mkdir()
#     #mkdir = make directory 
#     print(f"Created {start_time_path.parent}")

start_time_path.mkdir(exist_ok=True, parents=True)


print(start_time_path.is_dir())
print(start_time_path.is_file())

# w = scriere text
# r = citire text
# a = adaugare text
# wb = scriere binara
# rb = citire binara 
# ab = adaugare binara



# fis1 = open(start_time_path / "test.txt", "w")

# fis1.close()

now = datetime.now()
now_file_name = now.strftime("%Y%m%d_%H%M%S.txt")

#context manager

with open(start_time_path / now_file_name, "w") as fout:    #fout -> file descriptor (FD)
    fout.write("NO ERRORS!")

print("File operation done!")



# 1-fa un script care citeste de la tastatura numele cu input si creeaza un fisier in acelasi folder cu scriptul cu numele 1.txt in acre sa fie inputul 
# 2-fa un script in care e un generator care va da numerele lui Fibonacci, apeleaza next ori 100 ca sa extragi primele 100 numere si creeaza fisiere cu numele de la 1...100.txt 
# si in fiecare fisier sa fie pe rand fiecare numar din sirul lui Fibonacci. toate fisierele intr-un folder Fibonacci creat cu mkdir langa script 
# 3-read-only- afiseaza cand a fost programul ultima data de fiecare daca cand il pornesti cu time delta

