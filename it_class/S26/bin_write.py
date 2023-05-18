from pathlib import Path
import sys

ROOT = Path(__file__).parent

png_file_path = Path(sys.argv[1])

if not png_file_path.is_file():
    print("File not found.")
    sys.exit(1)

try:
    with open(png_file_path, "rb") as fin:
        content = fin.read()
except OSError as err:
    print(err)
    sys.exit(1)
else:
    try:
        with open(png_file_path.parent / f"1_{png_file_path.name}", "wb") as fout:
            fout.write(content[:(len(content) - 1) // 2])
        with open(png_file_path.parent / f"2_{png_file_path.name}", "wb") as fout:
            fout.write(content[:(len(content) - 1) // 2:])
    except OSError as err:
        print(err)




