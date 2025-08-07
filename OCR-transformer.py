import pytesseract

ENCARTE_DIR = "Desktop/Encartes-Concorrentes"

#Funtion to read files on PATH(ENCARTE_DIR)
def len_files_on_path():
    try:
        for files in ENCARTE_DIR:
            files(len[0-5])
    except:
        print("Não foi possivel encontrar os arquivos.")
     
def ocr_image_on_path():
    files = []
    ocr = pytesseract.image_to_string(ocr)
    try:
        for files in ENCARTE_DIR:
            files(ocr)
    except:
        print("Não foi possivel fazer o OCR do(s) arquivo(s)")