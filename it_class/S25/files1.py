from pathlib import Path

ROOT = Path(__file__).parent

input_file_path = ROOT / "ids.txt"

try:
    with open(input_file_path, "r") as fin:
        content = fin.read(10)
        print(content)
except OSError as err:
    print(err)
# else:
#     for i in content:
#         if i.startswith("#"):
#             print(i.strip("\n\r\t "))



