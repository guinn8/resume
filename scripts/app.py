from flask import Flask, render_template, send_from_directory, abort
import os
import json

app = Flask(__name__)

# Define the path to the 'job_postings' directory relative to 'scripts'
JOB_POSTINGS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'job_postings'))

def get_job_data():
    return [
        {
            'job_id': job_data.get('job_id', ''),
            'job_title': job_data.get('job_title', ''),
            'company_name': job_data.get('company', {}).get('name', ''),
            'location': job_data.get('location', ''),
            'employment_type': job_data.get('employment_type', ''),
            'md_link': os.path.join(company, position, md_file) if md_file else None,
            'pdf_link': os.path.join(company, position, pdf_file) if pdf_file else None
        }
        for company in os.listdir(JOB_POSTINGS_DIR)
        if os.path.isdir(os.path.join(JOB_POSTINGS_DIR, company))
        for position in os.listdir(os.path.join(JOB_POSTINGS_DIR, company))
        if os.path.isdir(os.path.join(JOB_POSTINGS_DIR, company, position))
        for json_file in os.listdir(os.path.join(JOB_POSTINGS_DIR, company, position, 'job_posting'))
        if json_file.endswith('.json')
        for job_data in [json.load(open(os.path.join(JOB_POSTINGS_DIR, company, position, 'job_posting', json_file)))]
        for md_file in [next((f for f in os.listdir(os.path.join(JOB_POSTINGS_DIR, company, position)) if f.endswith('.md') and 'letter' in f), None)]
        for pdf_file in [next((f for f in os.listdir(os.path.join(JOB_POSTINGS_DIR, company, position)) if f.endswith('.pdf') and 'letter' in f), None)]
    ]


@app.route('/')
def index():
    jobs = get_job_data()
    return render_template('index.html', jobs=jobs)

# Route to serve files from 'job_postings' directory
@app.route('/job_postings/<path:filename>')
def serve_job_postings(filename):
    # Securely serve files from 'job_postings'
    try:
        return send_from_directory(JOB_POSTINGS_DIR, filename)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
