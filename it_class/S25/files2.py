from pathlib import Path
import os

ROOT = Path(__file__).parent

input_file_path = ROOT / "git.txt"

try:
    with open(input_file_path, "r") as fin:
      print(fin.tell())
      fin.read()
      print(fin.tell())
      fin.seek(0, os.SEEK_SET)
      print(fin.tell())
      print(fin.read(10))
      fin.seek(0, os.SEEK_CUR)
      print(fin.tell())
except OSError as err:
    print(err)



   #1 char = 1 byte


