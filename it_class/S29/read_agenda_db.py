import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
TO_DB = ROOT / "phone.db"

connection = sqlite3.connect(TO_DB)
cursor = connection.cursor()

rows = cursor.execute(
    """SELECT * FROM agenda
    """)

names = []

for row in rows:
    id, name, tel = row
    names.append(name)
    print(row)

