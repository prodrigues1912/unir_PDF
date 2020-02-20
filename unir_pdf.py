'''

'''

import os
from PyPDF2 import PdfFileReader, PdfFileMerger

files_dir = ""  #indicar o caminho dos arquivos
pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
merger = PdfFileMerger()

print(os.listdir(files_dir))

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))

merger.write(os.path.join(files_dir, "pdf_unido.pdf"))

