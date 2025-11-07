# Test Files

This directory contains test files for the pdftotext program.

## Required Test Files

1. `sample_with_text.pdf`: A PDF file with searchable text
   - Should contain the word "sample" somewhere in the text
   - Should be a properly formatted PDF with embedded text

2. `sample_without_text.pdf`: A scanned PDF file without searchable text
   - Should be a scanned document
   - Should contain visible text in the image
   - Should NOT have embedded searchable text

3. `sample_image.png`: An image file containing text
   - Should be a clear image with readable text
   - PNG format preferred
   - Should contain visible text that OCR can detect

4. `invalid.xyz`: An invalid file
   - Can be any non-PDF file
   - Used for testing error handling