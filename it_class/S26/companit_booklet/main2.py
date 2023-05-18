import pickle
import json
from pathlib import Path

from lib.complaint import Complaint
from lib.interface import CLIMenu

ROOT = Path(__file__).parent

json_dump_path = ROOT / "complaint.json"

d1 = {
    "title": "Plangere",
    "text": "Prea mult Python pe ziua de azi",
    "resolved": False,
    "id": 1
}

# with open(json_dump_path, "w") as fout:
#     json.dump(d1, fout, indent=4)     #returneaza json deja formatat 


# with open(json_dump_path, "r") as fin: 
#     content = fin.read()
#     print(content)   #aici returneaza string

try:
    with open(json_dump_path, "r") as fin:
        json_content = json.load(fin)
        print(json_content)   #aici returneaza obiect python, dict
        print(json_content["resolved"])
except OSError:
    print("File not found!")
except json.JSONDecodeError:
    print("Invalid JSON file.")
else:
    print(json_content["resolved"])


#la fiecare json load try except si poti sa prinzi JSONDecodeError

