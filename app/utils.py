# Utility functions for the app
import os
import pdfplumber

def save_uploaded_file(file, upload_dir='uploads'):
	os.makedirs(upload_dir, exist_ok=True)
	filename = file.filename
	filepath = os.path.join(upload_dir, filename)
	file.save(filepath)
	return filename, filepath

def extract_text_from_pdf(filepath):
	text = ""
	with pdfplumber.open(filepath) as pdf:
		for page in pdf.pages:
			page_text = page.extract_text()
			if page_text:
				text += page_text
	return text
# Utility functions for the app
