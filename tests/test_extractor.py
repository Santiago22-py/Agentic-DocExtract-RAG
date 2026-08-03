"""
tests/test_extractor.py
Unit tests for PDF extraction service.
"""

import pytest
import io
from pypdf import PdfWriter
from src.services.extractor import extract_pdf_content, PDFExtractionError, ExtractedDocument


def create_sample_pdf_bytes(text_content: str = "Hello Agentic DocExtract!") -> bytes:
    """Helper utility to construct a valid PDF in-memory for testing."""
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    
    # Write to in-memory bytes
    buf = io.BytesIO()
    writer.write(buf)
    return buf.getvalue()


def test_extract_pdf_empty_bytes():
    """Test handling of empty 0-byte input."""
    with pytest.raises(PDFExtractionError) as exc_info:
        extract_pdf_content(b"")
    assert "empty" in str(exc_info.value).lower()


def test_extract_pdf_invalid_corrupt_bytes():
    """Test handling of invalid non-PDF content."""
    with pytest.raises(PDFExtractionError) as exc_info:
        extract_pdf_content(b"NOT_A_VALID_PDF_FILE_HEADER")
    assert "parse pdf" in str(exc_info.value).lower() or "failed" in str(exc_info.value).lower()


def test_extract_pdf_valid_content():
    """Test successful extraction of a generated PDF."""
    pdf_bytes = create_sample_pdf_bytes()
    result = extract_pdf_content(pdf_bytes)

    assert isinstance(result, ExtractedDocument)
    assert result.page_count == 1
    assert isinstance(result.extracted_text, str)
    assert isinstance(result.character_count, int)
