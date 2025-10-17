import os
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_uploaded_file(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return filename, filepath

def extract_text_from_pdf(filepath):
    return extract_text(filepath)
