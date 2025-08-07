import pandas
import re
import pdfplumber

ENCARTE_DIR = "Desktop/Encartes-Concorrentes"
files = "/OCR-Transformer"


def transformer_pdf():
    pdf = files[0]