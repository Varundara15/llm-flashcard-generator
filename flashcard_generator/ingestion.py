import os
from typing import Union
from pathlib import Path
import fitz

def read_txt(file_path : Union[str,Path]) -> str:
    if hasattr(file_path, "read"):  # Streamlit file uploader gives a file-like object
        return file_path.read().decode("utf-8")
    else:  # If it's a file path
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    
def read_pdf(file_path : Union[str,Path]) -> str:
    # If it's a file-like object (Streamlit), read bytes
    if hasattr(file_path, "read"):
        pdf_bytes = file_path.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    else:
        # It's a file path
        doc = fitz.open(file_path)

    text = ""
    for page in doc:
        text += page.get_text()
    return text
    
def ingest_input(file = None,raw_text :str = "") -> str:
    if file:
        filename = file.name
        suffix = Path(filename).suffix.lower()

        if suffix == ".pdf":
            return read_pdf(file)
        elif suffix == ".txt":
            return read_txt(file)
        else:
            raise ValueError("Unsupported file document. Please Upload pdf or txt files only!")
    
    elif raw_text.strip():
        return raw_text.strip()
    
    else:
        return ValueError("No text provided!")