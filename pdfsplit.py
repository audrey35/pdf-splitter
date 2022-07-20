import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# User Inputs
input_filename = "input_filename.pdf"
output_filename = "output_filename.pdf"
start_page = 481
end_page = 538

# PDF Split Program
script_folder = os.path.dirname(__file__) # relative path https://stackoverflow.com/a/918178
input_path = os.path.join(script_folder, input_filename)
output_path = os.path.join(script_folder, output_filename)
page_range = list(range(start_page - 1, end_page - 1)) # list of numbers b/w 2 values https://stackoverflow.com/a/18265979

# extract PDF pages https://learndataanalysis.org/how-to-extract-pdf-pages-and-save-as-a-separate-pdf-file-using-python/
pdf_reader = PdfFileReader(input_path) 
pdf_writer = PdfFileWriter()

for page in page_range:
  pdf_writer.addPage(pdf_reader.getPage(page))

with open(output_path, 'wb') as f:
    pdf_writer.write(f)
    f.close()