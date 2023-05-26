import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT / "phone.db"

class Database:

    def __init__(self, db_file_path: Path):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()
        #self.create_table_query = create_table_query

    #executati o metoda care creeaza tabelul pe baza queriului

    def create_table(self):
        self.cursor.execute(
            """ CREATE TABLE "primary" IF NOT EXISTS (
	        "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	        "email"	TEXT NOT NULL UNIQUE,
	        "name"	TEXT
            );"""
        )

    def read_all(self):
        rows = self.cursor.execute(
            """SELECT * FROM agenda""")   #numele tabelului se extrage din query de creare tabel
        for row in rows:
            print(row)
    
    def create_entry(self):
        self.name = input("Name: ")
        self.tel = input("Tel: ")
        self.cursor.execute(
            """INSERT INTO agenda ("name", "tel") VALUES (?, ?)""", (self.name, self.tel)
        )
        self.connection.commit()
        print(f"{self.name} with {self.tel} successfully added in the agenda.")
    
    def update_entry(self):
        # self.field = input("Field: ")
        # self.field2 = input("Field 2: ")
        self.cursor.execute(
            """UPDATE agenda SET tel = 0000 WHERE tel == 3333 """
        )
        self.connection.commit()
        

    def delete_entry(self):
        self.name = input("Name to delete: ")
        self.cursor.execute(
            """DELETE FROM agenda WHERE name == ? """, (self.name, )
        )
        self.connection.commit()
        print(f"{self.name} successfully deleted.")


d1 = Database(DB_PATH)

# d1.update_entry()
d1.read_all()