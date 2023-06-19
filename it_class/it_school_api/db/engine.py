from sqlalchemy import create_engine
from settings import ROOT

DB_PATH = ROOT / "db.sqlite3"

engine = create_engine(f"sqlite:////{DB_PATH}", echo=True)
