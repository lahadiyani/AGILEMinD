# app/loaders/custom/pdf_loader.py

from app.loaders.base_loader import BaseLoader
from app.loaders.utils import validate_path
from PyPDF2 import PdfReader

class PDFLoader(BaseLoader):
    """
    Loader untuk membaca file PDF dan mengembalikan list halaman (sebagai string).
    """

    def __init__(self, max_pages: int = None):
        self.max_pages = max_pages

    def load(self, source: str) -> list[str]:
        validate_path(source)

        reader = PdfReader(source)
        pages = reader.pages[:self.max_pages] if self.max_pages else reader.pages
        return [page.extract_text() for page in pages]
