import re
from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter

def preprocess_text(text : str) -> str:
    text = re.sub(r'\s+', ' ', text)        # Collapse multiple spaces/tabs/newlines
    text = re.sub(r'\n{2,}', '\n', text)    # Collapse multiple blank lines
    return text.strip()


def chunk_txt(text:str,chunk_size :int = 800, chunk_overlap :int = 200) -> List[str]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
    )
    chunks = splitter.split_text(text)
    return chunks