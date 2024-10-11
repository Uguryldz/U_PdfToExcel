import os
import logging
from datetime import datetime
from flask import Flask, request
import pdfplumber
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Sabit log dizini
log_dir = r"C:\U_PdfToExcel\logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Log dosya adı: yyyyMMdd_HHmmapp.log
log_filename = datetime.now().strftime("%Y%m%d_%H%M_app.log")
log_path = os.path.join(log_dir, log_filename)

# Log başlangıç mesajı
with open(log_path, 'w', encoding='utf-8') as log_file:
    log_file.write("Bu proje Uğur Yıldız tarafından derlenmiştir. https://www.linkedin.com/in/uguryldz/\n")

# Log ayarları
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files or 'output_path' not in request.form:
        logging.error("No file part or output path")
        return "No file part or output path", 400
    
    file = request.files['file']
    output_path = request.form['output_path']

    if file.filename == '':
        logging.error("No selected file")
        return "No selected file", 400
    
    wb = Workbook()
    ws_text = wb.active
    ws_text.title = "U_TextContent"
    ws_tables = wb.create_sheet(title="U_Tables")

    try:
        with pdfplumber.open(file.stream) as pdf:
            for page_number in range(len(pdf.pages)):
                page = pdf.pages[page_number]
                text = page.extract_text()

                if text:
                    ws_text.append([f"Text from Page {page_number + 1}:"])
                    for line in text.split('\n'):
                        ws_text.append([line])
                    ws_text.append([])

                tables = page.extract_tables()
                if tables:
                    ws_tables.append([f"Tables from Page {page_number + 1}:"])
                    for table in tables:
                        df_table = pd.DataFrame(table)
                        for row in dataframe_to_rows(df_table, index=False, header=False):
                            ws_tables.append(row)
                        ws_tables.append([])

        wb.save(output_path)
        logging.info(f"Excel dosyasi başariyla kaydedildi: {output_path}")
        return f"Excel dosyası başarıyla kaydedildi: {output_path}", 200

    except Exception as e:
        logging.error(f"Hata olustu: {e}")
        return f"Hata oluştu: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089)
