'''
Python PyMudf Implementation
'''
import sys, pathlib,fitz
with fitz.open("./NCF2023.pdf") as doc:  # open document
    text = chr(12).join([page.get_text() for page in doc])
# write as a binary file to support non-ASCII characters
pathlib.Path("output" + ".txt").write_bytes(text.encode())

'''
Python PDFQuery Implementation
'''
