#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the PDF to Text Converter.

Tests both text extraction and OCR functionality with various types of input files.

Copyright (c) 2025 NJC Software LLC
Licensed under the MIT License. See LICENSE file for details.
"""

import os
import sys
import unittest
import tempfile
from pathlib import Path

# Add parent directory to Python path to import pdftotext
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pdftotext import extract_text_from_pdf, ocr_pdf

class TestPDFToText(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up test files directory
        cls.test_files_dir = Path(__file__).parent / 'test_files'
        cls.pdf_with_text = cls.test_files_dir / 'sample_with_text.pdf'
        cls.pdf_without_text = cls.test_files_dir / 'sample_without_text.pdf'
        cls.image_file = cls.test_files_dir / 'sample_image.png'
        cls.invalid_file = cls.test_files_dir / 'invalid.xyz'

    def setUp(self):
        # Create a temporary directory for output files
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Clean up temporary files
        for file in Path(self.temp_dir).glob('*'):
            file.unlink()
        os.rmdir(self.temp_dir)

    def test_extract_text_from_searchable_pdf(self):
        """Test extracting text from a PDF with searchable text"""
        result = extract_text_from_pdf(self.pdf_with_text)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertIn('sample', result.lower())

    def test_extract_text_from_scanned_pdf(self):
        """Test extracting text from a PDF without searchable text (scanned)"""
        result = extract_text_from_pdf(self.pdf_without_text)
        self.assertTrue(result == '' or result is None)  # Should return empty string or None for non-searchable PDFs

    def test_ocr_on_scanned_pdf(self):
        """Test OCR functionality on a scanned PDF"""
        output_path = Path(self.temp_dir) / 'ocr_output.pdf'
        result = ocr_pdf(self.pdf_without_text, output_path)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_ocr_on_image(self):
        """Test OCR functionality on an image file"""
        output_path = Path(self.temp_dir) / 'image_ocr_output.pdf'
        result = ocr_pdf(self.image_file, output_path)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_invalid_file(self):
        """Test error handling with an invalid file"""
        result = extract_text_from_pdf(self.invalid_file)
        self.assertIsNone(result)

    def test_nonexistent_file(self):
        """Test error handling with a nonexistent file"""
        result = extract_text_from_pdf(Path(self.temp_dir) / 'nonexistent.pdf')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()