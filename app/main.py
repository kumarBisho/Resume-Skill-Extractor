
from flask import Flask, request, render_template, redirect, url_for
from app.models import db, Resume
from app.parser import extract_resume_info
from app.utils import save_uploaded_file, extract_text_from_pdf
import os
from datetime import datetime

import pymysql
pymysql.install_as_MySQLdb()


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL', 'sqlite:///resume.db')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.before_request
    def create_tables():
        db.create_all()

    @app.route('/', methods=['GET'])
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
                filename, filepath = save_uploaded_file(file)
                text = extract_text_from_pdf(filepath)
                extracted_data = extract_resume_info(text)
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
        results = Resume.query.filter(Resume.skills.ilike(f'%{skill}%')).all()
        return render_template('index.html', search_results=results)

    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app = create_app()
    app.run(host='0.0.0.0', port=port, debug=True)