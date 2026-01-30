from flask import Flask, render_template, request, abort
import csv

app = Flask(__name__)
CSV_FILE = "jobs.csv"

def load_jobs():
    jobs = []
    with open('jobs.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            jobs.append(row)
    return jobs
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/')
@app.route('/jobs')
def jobs():
    jobs = load_jobs()

    # Get filters from URL
    keyword = request.args.get('keyword', '').lower()
    location = request.args.get('location', '').lower()
    experience = request.args.get('experience', '').lower()
    min_salary = request.args.get('min_salary', '')
    max_salary = request.args.get('max_salary', '')

    filtered_jobs = []

    for job in jobs:
        if keyword and keyword not in (
            job['job_title'] + job['company'] + job['skills']
        ).lower():
            continue

        if location and location not in job['location'].lower():
            continue

        if experience and experience not in job['experience'].lower():
            continue

        if min_salary and int(job['salary_min']) < int(min_salary):
            continue

        if max_salary and int(job['salary_max']) > int(max_salary):
            continue

        filtered_jobs.append(job)

    return render_template(
        'jobs.html',
        jobs=filtered_jobs
    )
    return render_template("jobs.html", jobs=jobs)

@app.route('/job/<job_id>')
def job_detail(job_id):
    jobs = load_jobs()
    for job in jobs:
        if job['job_id'] == job_id:
            return render_template('job_detail.html', job=job)
    abort(404)
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")


if __name__ == "__main__":
    app.run(debug=True)
