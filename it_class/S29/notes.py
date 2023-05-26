import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_FILE = ROOT / "db2.db"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

rows = cursor.execute("SELECT * FROM users;")

print(rows.fetchall())


