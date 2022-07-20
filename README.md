# PDF Splitter
Python script that creates a new pdf by extracting a subset of pages from an existing pdf.

## How to use PDF Splitter
1. Download the files for this repo by cloning or as a zip.
2. Add the pdf you want to split in the root directory containing pdfsplit.py
3. Edit pdfsplit.py
   - update input_filename, output_filename, start_page, and end_page
   - input pdf is assumed to be located in the same directory as pdfsplit.py
   - output pdf will be generated in the directory containing pdfsplit.py
   - start_page and end_page are pages in input_file
4. Open a console.
5. Navigate to the directory containing the pdfsplit.py
6. Run `pipenv install` to install PyPDF2
   - if pipenv creates a .venv folder in a directory that doesn't contain pdfsplit.py, remove the virtual environment: `pipenv --rm`
   - go to the folder that the .venv was erroneously created in, delete the Pipfile in the directory
   - rerun `pipenv install` to install PyPDF2
7. Run `python pdfsplit.py` to generate the new pdf
