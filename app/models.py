from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(100))
    skills = db.Column(db.Text)
    experience = db.Column(db.Text)
    uploaded_date = db.Column(db.DateTime, default=datetime.utcnow)
