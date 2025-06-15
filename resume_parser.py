from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pdfplumber
import os
import re
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    skills = db.Column(db.String(500))
    experience = db.Column(db.Text)
    uploaded_date = db.Column(db.DateTime)

def create_tables():
    with app.app_context():
        db.create_all()

def extract_resume_info(text):
    # Extract name (assuming it's at the top)
    name = text.split('\n')[0].strip()
    
    # Extract email using regex
    email = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    email = email.group(0) if email else "Not found"
    
    # Extract phone number using regex
    phone = re.search(r'\+?\d{10,12}', text)
    phone = phone.group(0) if phone else "Not found"
    
    # Extract skills (common keywords)
    skills = []
    skill_keywords = [
        'python', 'java', 'javascript', 'sql', 'html', 'css', 'c++', 'c#', 'react', 'node.js',
        'git', 'github', 'docker', 'machine learning', 'nlp', 
        'data structure and algorithms', 'oops'
    ]
    
    # Clean text for better matching
    text_lower = text.lower()
    
    # Extract skills with improved matching
    for keyword in skill_keywords:
        # Handle multi-word skills
        if ' ' in keyword:
            # Check for exact phrase match
            if keyword in text_lower:
                skills.append(keyword.title())
        else:
            # For single-word skills, use regex to find variations
            if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                skills.append(keyword.title())
    
    # Extract experience (lines containing company names)
    experience = []
    lines = text.split('\n')
    for line in lines:
        if any(word in line.lower() for word in ['company', 'experience', 'engineer', 'developer']):
            experience.append(line.strip())
    
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'skills': ', '.join(skills),
        'experience': '\n'.join(experience)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and file.filename.endswith('.pdf'):
        try:
            # Save the file
            filename = file.filename
            filepath = os.path.join('uploads', filename)
            os.makedirs('uploads', exist_ok=True)
            file.save(filepath)
            
            # Extract text from PDF
            text = ""
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    text += page.extract_text()
            
            # Extract information
            extracted_data = extract_resume_info(text)
            
            # Save to database
            with app.app_context():
                resume = Resume(
                    filename=filename,
                    name=extracted_data['name'],
                    email=extracted_data['email'],
                    phone=extracted_data['phone'],
                    skills=extracted_data['skills'],
                    experience=extracted_data['experience'],
                    uploaded_date=datetime.now()
                )
                db.session.add(resume)
                db.session.commit()
            
            return render_template('index.html', result=extracted_data)
            
        except Exception as e:
            return render_template('index.html', error=str(e))
    
    return redirect(url_for('index'))

@app.route('/search')
def search():
    skill = request.args.get('skill', '').lower()
    if not skill:
        return redirect(url_for('index'))
    
    with app.app_context():
        results = Resume.query.filter(Resume.skills.ilike(f'%{skill}%')).all()
    return render_template('index.html', search_results=results)

if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=5000)
