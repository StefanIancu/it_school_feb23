from datetime import datetime
from pathlib import Path

now = datetime.now()

script_path = Path(__file__)
new_folder = script_path.parent / "last_time" / "last_time.txt"

new_folder.mkdir(exist_ok=True, parents=True)
folder_name = "last_time.txt"

delta = now - ?

with open(new_folder / folder_name, "w") as fout:
    fout.write(str(now))

print("Exec done.")

