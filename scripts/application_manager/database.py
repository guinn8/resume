# database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(255))
    company_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    job_description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    benefits = db.Column(db.Text)
    application_deadline = db.Column(db.Date)
    contact_information = db.Column(db.String(255))

    def __repr__(self):
        return f'<JobPosting {self.job_title} at {self.company_name}>'
