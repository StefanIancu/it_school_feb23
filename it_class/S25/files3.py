from pathlib import Path
import os

ROOT = Path(__file__).parent

input_file_path = ROOT / "git.txt"

#citire de la sfarsitul documentului / coada 

try:
    with open(input_file_path, "r") as fin:
        end = fin.seek(0, os.SEEK_END)
        fin.seek(end - 10, os.SEEK_SET)
        print(fin.read())
except OSError as err:
    print(err)



   #1 char = 1 byte