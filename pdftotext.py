#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF to Text Converter with OCR support.

This tool extracts text from PDF files, with support for both searchable PDFs
and scanned documents (using OCR). It can output to file or stdout and includes
filtering capabilities.

Copyright (c) 2025 NJC Software LLC
Licensed under the MIT License. See LICENSE file for details.
"""

import os
import sys
import argparse
import pdfplumber
from img2pdf import convert
import pytesseract
import tempfile
import glob
import shutil

def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print("Error extracting text from PDF:", e, file=sys.stderr)
        return None

def ocr_pdf(input_path, output_path):
    try:
        input_path = str(input_path)
        # Check if input is already a PDF
        if input_path.lower().endswith('.pdf'):
            # Convert PDF to image first using ImageMagick
            # convert all pages of the PDF to PNG images in a temporary directory
            tmp_dir = tempfile.mkdtemp(prefix="pdftoimg_")
            try:
                out_pattern = os.path.join(tmp_dir, "page-%03d.png")
                cmd = f"convert -density 300 -quality 100 -background white -alpha remove '{input_path}' '{out_pattern}'"
                if os.system(cmd) != 0:
                    raise RuntimeError("ImageMagick convert failed")

                # OCR each generated image and concatenate results
                text_parts = []
                for img_path in sorted(glob.glob(os.path.join(tmp_dir, "page-*.png"))):
                    text_parts.append(pytesseract.image_to_string(img_path))

                return "\n".join(text_parts).strip()
            finally:
                # cleanup temporary images
                try:
                    shutil.rmtree(tmp_dir)
                except Exception:
                    pass    
        else:
            # For image files, convert to PDF first
            with open(output_path, 'wb') as pdf:
                img = convert([input_path])
                pdf.write(img)
            # Use tesseract directly on the input image
            return pytesseract.image_to_string(input_path)
    except Exception as e:
        print(f"Error during OCR processing: {e}", file=sys.stderr)
        return None

def write_output(text, output_path=None, filter_word=None):
    if text is None:
        return

    # Filter text if a word is specified
    if filter_word:
        text = '\n'.join(line for line in text.splitlines() if filter_word.lower() in line.lower())

    # Write to file if output path is specified, otherwise print to stdout
    if output_path:
        with open(output_path, 'w') as txt:
            txt.write(text)
        print(f"Text has been written to {output_path}", file=sys.stderr)
    else:
        print(text)

def main():
    parser = argparse.ArgumentParser(description='Extract text from PDF files with optional OCR support')
    parser.add_argument('input_pdf', help='Path to the input PDF file')
    parser.add_argument('-o', '--output', help='Path to the output text file (if not specified, prints to stdout)')
    parser.add_argument('-f', '--filter', help='Only output lines containing this word')
    args = parser.parse_args()

    text = extract_text_from_pdf(args.input_pdf)
    if text:
        print("PDF contains extractable text.", file=sys.stderr)
        write_output(text, args.output, args.filter)
    else:
        print("PDF does not contain extractable text. Attempting OCR...", file=sys.stderr)
        temp_ocr_pdf = "temp_ocr_output.pdf"
        os.system(f"convert '{args.input_pdf}' '{temp_ocr_pdf}'")
        text = ocr_pdf(args.input_pdf, temp_ocr_pdf)
        if text:
            print("OCR completed successfully.", file=sys.stderr)
            write_output(text, args.output, args.filter)
        else:
            print("Error converting PDF to text.", file=sys.stderr)
            sys.exit(1)
        
        # Clean up temporary file
        if os.path.exists(temp_ocr_pdf):
            os.remove(temp_ocr_pdf)

if __name__ == "__main__":
    main()
