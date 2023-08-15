'''
Python PyMudf Implementation
'''
import sys, pathlib,fitz
with fitz.open("./NCF2023.pdf") as doc:  # open document
    text = chr(12).join([page.get_text() for page in doc])
# write as a binary file to support non-ASCII characters
pathlib.Path("PyMuPDF_output" + ".txt").write_bytes(text.encode())

'''
Python PDFQuery Implementation
'''
import pdfquery
pdf = pdfquery.PDFQuery('NCF2023.pdf')
pdf.load()
pdf.tree.write('pdfquery_output.xml', pretty_print = True)

'''
PDF PdfPlumber Implementation
'''
import pdfplumber
with pdfplumber.open("NCF2023.pdf") as pdf:
    page = pdf.pages[12]
    print(page.chars)
    print(page.extract_text)
