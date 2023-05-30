from pathlib import Path
import shutil
import time

WATCHED_DIR = Path("/Users/stefantraianiancu/Desktop/it_school/it_class/S30/downloads")
TARGET_DIR = Path("/Users/stefantraianiancu/Desktop/it_school/it_class/S30/clean_downloads")

CATEGORY_MAP = {
        "audio": ["mp3", "wav", "flac"],
        "documents":["doc", "docx", "xls", "xlsx", "pdf", "txt"],
        "pictures": ["jpg", "jpeg", "png", "bmp"]
    }


def categorize(file_path: Path, category: str):
    category_dir = TARGET_DIR / category
    category_dir.mkdir(exist_ok=True)

    file_name = file_path.name
    dst_path = category_dir / file_name

    # shutil.copy2(str(file_path), str(dst_path))    - copy
    shutil.move(str(file_path), str(dst_path))          #-move
    # shutil.copytree()                               #copy dir cu tot cu continut
    #shutil.rmtree       #delete 


def get_category(path: Path):
    extension = path.suffix.strip(".")
    for k, v in CATEGORY_MAP.items():
        if extension in v:
            return k
    return "misc"


def walk(root_dir: Path):
    for path in root_dir.iterdir():
        if path.is_file():
            categorize(path, get_category(path))


def watch(dir: Path):
    prev_m_time = dir.stat().st_mtime


    while True:
        time.sleep(0.1)
        m_time = dir.stat().st_mtime

        if m_time > prev_m_time:
            walk(dir)
            prev_m_time = m_time


watch(WATCHED_DIR)

