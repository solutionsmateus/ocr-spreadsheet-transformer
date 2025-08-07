import cv2
import pytesseract
import pandas as pd
import os
from PIL import Image

#Make OCR Transformer to Excel Spreadsheet.

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

caminho_imagem = r'OCR-Transformer\encarte_teste.jpeg'
diretorio_base = os.path.dirname(caminho_imagem)

img = cv2.imread(caminho_imagem)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

temp_path = os.path.join(diretorio_base, 'temp_ocr.png')
cv2.imwrite(temp_path, thresh)

texto = pytesseract.image_to_string(Image.open(temp_path))

linhas = [linha.strip() for linha in texto.split('\n') if linha.strip()]

df = pd.DataFrame(linhas, columns=['Texto Extraído'])

saida = os.path.join(diretorio_base, 'resultado_ocr.xlsx')
df.to_excel(saida, index=False)

os.remove(temp_path)

print(f'OCR finalizado com sucesso. Planilha salva em: {saida}')

rows = 

columms = 

#Organization of Excel Spreadsheet.

def organize_spreadsheet():
    saida_spreadsheet = len(saida)
