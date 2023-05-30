import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
PHOTO_PATH = ROOT / "poze_nunta"

#1st level iteration

# print(os.listdir(ROOT)) --- one way

# for i in ROOT.iterdir():
#     print(i, i.is_dir())       ---- another way, preferable

# for dirpath, dirs, files in os.walk(ROOT):
#     # print(f"In directorul {dirpath} am gasit {len(dirs)} directoare si {len(files)} fisiere.") #---intra in fiecare dir si printeaza ce are inauntru
#     for _file in files:
#         print(Path(dirpath) / _file)

# for i in PHOTO_PATH.glob("**/*.jpg"):       # ----- glob = un fel de wildcard Linux, functioneaza la fel, itereeaza si subdirectoare
#     print(i)   


# #BULK RENAME

# count = 0
# for i in PHOTO_PATH.glob("*.jpg"):
#     i.rename(PHOTO_PATH / f"Andreea&Andrei_{count}.jpg")
#     count += 1

