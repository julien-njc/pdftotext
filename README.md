# PDF to Text Converter

A Python utility to extract text from PDF files with OCR support. This tool can extract text from both searchable PDFs and scanned documents (using OCR).

## Features

- Extract text from searchable PDFs
- OCR support for scanned documents
- Output to file or stdout
- Text filtering capabilities
- Pipe-friendly output format
- Automatic cleanup of temporary files

## Requirements

- Python 3.x
- pdfplumber
- img2pdf
- pytesseract
- ImageMagick (for the `convert` command)

## Installation

1. Ensure you have Python 3.x installed
2. Install the required Python packages using the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```
3. Install ImageMagick:
   ```bash
   # On macOS using Homebrew
   brew install imagemagick
   
   # On Ubuntu/Debian
   sudo apt-get install imagemagick
   ```

## Usage

### Basic Usage

Extract text from a PDF and save to a file:
```bash
python pdftotext.py input.pdf -o output.txt
```

### Print to stdout
Useful for viewing content directly or piping to other commands:
```bash
python pdftotext.py input.pdf
```

### Filter Content
Only output lines containing specific text:
```bash
python pdftotext.py input.pdf -f water
```

### Combine Output File and Filtering
Save filtered content to a file:
```bash
python pdftotext.py input.pdf -o filtered.txt -f water
```

### Use with Pipes
The script works well with Unix pipes:
```bash
python pdftotext.py input.pdf | grep "water"
```

## Command Line Arguments

- `input_pdf` (required): Path to the input PDF file
- `-o, --output`: Path to the output text file (if not specified, prints to stdout)
- `-f, --filter`: Only output lines containing this word (case-insensitive)

## Notes

- Status messages are printed to stderr to ensure clean pipe operations
- OCR is automatically attempted if text extraction fails
- Temporary files are automatically cleaned up after processing

## Testing

The project includes a comprehensive test suite that validates:
- Text extraction from searchable PDFs
- OCR processing of scanned PDFs
- OCR processing of image files
- Error handling for invalid files

To run the tests:

1. Add the required test files to `tests/test_files/` (see `tests/test_files/README.md` for details)
2. Run the tests:
   ```bash
   python -m unittest discover tests
   ```

### Test Files Required
- `tests/test_files/sample_with_text.pdf`: A PDF with searchable text
- `tests/test_files/sample_without_text.pdf`: A scanned PDF without searchable text
- `tests/test_files/sample_image.png`: An image file containing text
- `tests/test_files/invalid.xyz`: Any non-PDF file for error testing

## Creating a Standalone Executable

You can create a standalone executable that will run on other Mac computers without requiring Python or dependencies to be installed:

1. Install the build requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Create the standalone executable:
   ```bash
   pyinstaller pdftotext.spec
   ```

The executable will be created in the `dist` directory. You can copy the `dist/pdftotext` file to any Mac computer and run it directly:
```bash
./pdftotext input.pdf -o output.txt
```

Note: The target Mac computer still needs to have ImageMagick installed for OCR functionality:
```bash
brew install imagemagick
```