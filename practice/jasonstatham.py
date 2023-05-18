import json
from pathlib import Path

ROOT = Path(__file__).parent / "test.json"

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


#create a .json with the dictionary above  - encode


# try:
#     with open(ROOT, "w") as fout:
#         content = json.dump(x, fout, indent=4)
# except OSError as err:
#     print(err)
# except json.JSONDecodeError as err:
#     print(err)
# else:
#     print("Execution successful - json file created.")

 
#read from a .json an return an object   - decode

try:
    with open(ROOT, "r") as fin:
        content = json.load(fin)
        #print(content)
        print(content)
except OSError as err:
    print(err)
except json.JSONDecodeError as err:
    print(err)
else:
    print("Reading successfully.")


print(type(content))




