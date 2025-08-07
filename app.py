from flask import Flask

app = Flask(__name__)

FILE_OCR_TRANSFORMER_PATH = 'OCR-Transformer\OCR-transformer.py'
FILE_SPREADSHEET_TRANSFORMER_PATH = 'OCR-Transformer\Spreadsheet-transformer.py'
    
    
    
if __name__ == 'main':
    app.run(Debug=True)