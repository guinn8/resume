# backend.py

from flask import Flask, request, jsonify, render_template, redirect, url_for
from database import db, JobPosting
from ai_processing_module import process_job_posting
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_postings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        unstructured_text = request.form['unstructured_text']
        structured_data = process_job_posting(unstructured_text)
        return render_template('edit_posting.html', data=structured_data)
    return render_template('index.html')

from datetime import datetime

@app.route('/save', methods=['POST'])
def save_posting():
    data = request.form
    application_deadline = None

    # Attempt to parse the application deadline if provided
    deadline_str = data.get('application_deadline')
    if deadline_str not in [None, '']:
        try:
            application_deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
        except ValueError:
            # Log the error or provide feedback if needed
            print(f"Invalid date format for application_deadline: {deadline_str}")
            application_deadline = None  # Set to None or handle differently if needed

    job_posting = JobPosting(
        job_title=data.get('job_title'),
        company_name=data.get('company_name'),
        location=data.get('location'),
        job_description=data.get('job_description'),
        requirements=data.get('requirements'),
        benefits=data.get('benefits'),
        application_deadline=application_deadline,
        contact_information=data.get('contact_information'),
    )
    
    db.session.add(job_posting)
    db.session.commit()
    return redirect(url_for('view_postings'))

@app.route('/postings', methods=['GET'])
def view_postings():
    postings = JobPosting.query.all()
    return render_template('view_postings.html', postings=postings)

@app.route('/posting/<int:posting_id>', methods=['GET'])
def view_posting(posting_id):
    posting = JobPosting.query.get_or_404(posting_id)
    return render_template('view_posting.html', posting=posting)

if __name__ == '__main__':
    app.run(debug=True)
