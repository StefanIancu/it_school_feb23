import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
PHOTO_PATH = ROOT / "poze_nunta"

#1st level iteration

# print(os.listdir(ROOT)) --- one way

suffix = "while.py"

for i in ROOT.iterdir():
    i_str = str(i)
    print(i, i.is_dir())      # ---- another way, preferable
   

# for dirpath, dirs, files in os.walk(ROOT):
#     # print(f"In directorul {dirpath} am gasit {len(dirs)} directoare si {len(files)} fisiere.") #---intra in fiecare dir si printeaza ce are inauntru
#     for _file in files:
#         print(Path(dirpath) / _file)