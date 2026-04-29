#!/usr/bin/env python3
"""
PDF text extractor for paper-reader skill.

Usage:
    python parse_pdf.py <pdf_path>

Output: extracted text with page markers like [PAGE 1], [PAGE 2]...
"""

import sys
import json
from pathlib import Path

def extract_text(pdf_path):
    """Extract text from PDF with page markers."""
    try:
        import pdfplumber
    except ImportError:
        print("ERROR: pdfplumber not installed. Run: pip install pdfplumber", file=sys.stderr)
        sys.exit(1)

    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"ERROR: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    all_text = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for i, page in enumerate(pdf.pages):
            all_text.append(f"\n[PAGE {i+1}]\n")
            text = page.extract_text()
            if text:
                all_text.append(text)

    return "\n".join(all_text)


def extract_metadata(pdf_path):
    """Try to extract metadata from PDF."""
    try:
        import pdfplumber
    except ImportError:
        return {}

    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            meta = pdf.metadata
            return meta if meta else {}
    except Exception:
        return {}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_pdf.py <pdf_path>", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]

    if "--metadata" in sys.argv:
        meta = extract_metadata(pdf_path)
        print(json.dumps(meta, ensure_ascii=False, indent=2))
    else:
        text = extract_text(pdf_path)
        print(text)
