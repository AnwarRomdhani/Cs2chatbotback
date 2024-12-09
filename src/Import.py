import os
from PyPDF2 import PdfReader

def get_pdf_text():
    # Dynamically compute the absolute path of the PDF file
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
    pdf_path = os.path.join(base_dir, 'docs', 'Cs2_pro_guide.pdf')  # Adjust to your folder structure

    # Read the PDF
    reader = PdfReader(pdf_path)
    pdf = ""
    for page in reader.pages:
        pdf += page.extract_text()
    return pdf