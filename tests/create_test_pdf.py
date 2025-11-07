#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test file generator: Creates a sample PDF with searchable text.

Copyright (c) 2025 NJC Software LLC
Licensed under the MIT License. See LICENSE file for details.
"""

from fpdf import FPDF

def create_sample_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Sample PDF with Searchable Text", ln=1, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This is a test document containing searchable text.", ln=1, align="L")
    pdf.cell(200, 10, txt="It includes the word 'sample' and some numbers: 12345", ln=1, align="L")
    pdf.cell(200, 10, txt="This text should be easily extractable.", ln=1, align="L")
    pdf.output("tests/test_files/sample_with_text.pdf")

if __name__ == "__main__":
    create_sample_pdf()