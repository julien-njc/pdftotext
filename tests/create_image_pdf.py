#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test file generator: Creates a non-searchable PDF from an image.

Copyright (c) 2025 NJC Software LLC
Licensed under the MIT License. See LICENSE file for details.
"""

from PIL import Image
import img2pdf

def create_image_pdf():
    # First convert PNG to JPEG (img2pdf works better with JPEG)
    img = Image.open("tests/test_files/sample_image.png")
    rgb_img = img.convert('RGB')
    rgb_img.save("tests/test_files/temp.jpg")
    
    # Convert JPEG to PDF
    with open("tests/test_files/sample_without_text.pdf", "wb") as f:
        f.write(img2pdf.convert("tests/test_files/temp.jpg"))

if __name__ == "__main__":
    create_image_pdf()