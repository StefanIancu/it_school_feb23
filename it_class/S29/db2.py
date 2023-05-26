from db import Database
import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_FILE = ROOT / "db2.db"

db = Database(DB_FILE)
db.read_all()