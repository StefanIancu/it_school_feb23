import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_FILE = ROOT / "db2.db"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

email = input("Email: ")
name = input("Name: ")

cursor.execute("""INSERT INTO users (email, name) VALUES (?, ?);""", (email, name))     #nu pune doar 1 pt ca argumentul doi trebuie sa fie tuplu, poti pune = (1,)
connection.commit()

rows = cursor.execute ("SELECT * FROM USERS;")

for row in rows:
    print(row)


