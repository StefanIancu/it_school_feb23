from PyPDF2 import PdfReader
from pathlib import Path

ROOT = Path(__file__).parent
PDF_PATH = ROOT / "Joshua Bloch - Effective Java.pdf"

reader = PdfReader(PDF_PATH)
page = reader.pages[11]

#len(reader.pages) - len of the pdf
print(page.extract_text())
