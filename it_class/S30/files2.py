from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent

FILE_PATH = ROOT / "code1.txt"

c_time = FILE_PATH.stat().st_mtime

#at time accesed time
#mttime modified time
#cttime creation time

c_date_time = datetime.fromtimestamp(c_time)
print(c_date_time)  #.strftime pt format la propria dorinta

