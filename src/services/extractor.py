"""
src/services/extractor.py
Service module responsible for reading and extracting text & metadata from PDF documents.
"""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
import io
from pypdf import PdfReader
from pypdf.errors import PyPdfError, PdfReadError


class PDFExtractionError(Exception):
    """Custom exception raised when PDF parsing or extraction fails."""
    pass


class ExtractedDocument(BaseModel):
    """
    Pydantic schema representing the structured result of a PDF extraction.
    """
    extracted_text: str = Field(..., description="Full text extracted from all pages combined.")
    page_count: int = Field(..., description="Total number of pages in the PDF.")
    character_count: int = Field(..., description="Total character length of extracted text.")
    page_breakdown: List[str] = Field(default_factory=list, description="Text broken down page-by-page.")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Extracted PDF metadata properties.")


def extract_pdf_content(file_bytes: bytes) -> ExtractedDocument:
    """
    Extracts text and metadata from PDF bytes.

    :param file_bytes: Raw binary content of the PDF file.
    :return: ExtractedDocument model with text, metrics, and metadata.
    :raises PDFExtractionError: If the PDF is corrupted, encrypted, or unparseable.
    """
    if not file_bytes:
        raise PDFExtractionError("Provided file content is empty (0 bytes).")

    try:
        stream = io.BytesIO(file_bytes)
        reader = PdfReader(stream)

        # Handle encrypted PDFs that require a password
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception:
                raise PDFExtractionError("PDF document is encrypted and password-protected.")

        page_texts: List[str] = []
        for page in reader.pages:
            text = page.extract_text() or ""
            page_texts.append(text.strip())

        full_text = "\n\n".join(page_texts).strip()

        parsed_metadata: Dict[str, Any] = {}
        if reader.metadata:
            for key, value in reader.metadata.items():
                clean_key = key.lstrip("/")
                parsed_metadata[clean_key] = str(value) if value else None

        return ExtractedDocument(
            extracted_text=full_text,
            page_count=len(reader.pages),
            character_count=len(full_text),
            page_breakdown=page_texts,
            metadata=parsed_metadata
        )

    except (PyPdfError, PdfReadError) as err:
        raise PDFExtractionError(f"Failed to parse PDF document: {str(err)}") from err
    except Exception as err:
        if isinstance(err, PDFExtractionError):
            raise
        raise PDFExtractionError(f"Unexpected error during PDF processing: {str(err)}") from err
