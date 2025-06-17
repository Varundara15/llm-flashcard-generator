import os
from typing import Union
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
import tempfile

def read_txt(file_path : Union[str,Path]) -> str:
    if hasattr(file_path, "read"):  # Streamlit file uploader gives a file-like object
        return file_path.read().decode("utf-8")
    else:  # If it's a file path
        loader = TextLoader(str(file_path),encoding = "utf-8")
        documents = loader.load()
        return "\n".join(doc.page_content for doc in documents)
    
def read_pdf(file_path : Union[str,Path]) -> str:
    # If it's a file-like object (Streamlit), read bytes
    if hasattr(file_path, "read"):
        pdf_bytes = file_path.read()
        
        with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:
            tmp.write(pdf_bytes)
            tmp_path = tmp.name

        loader = PyMuPDFLoader(tmp_path)
        documents = loader.load()
        os.remove(tmp_path)
    else:
        loader = PyMuPDFLoader(str(file_path))
        documents = loader.load()
    return "\n".join(doc.page_content for doc in documents)

    
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