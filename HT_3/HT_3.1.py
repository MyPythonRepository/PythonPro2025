from flask import Flask, render_template_string, send_from_directory
from faker import Faker
import csv
import os
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

app = Flask(__name__)
faker_instance = Faker("uk_UA")


UPLOAD_FOLDER = 'my_generated_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# http://localhost:5000/generate_students?count=25
@app.route("/generate_students")
@use_kwargs(
    {
        "count": fields.Int(
            missing=10,
            validate=validate.Range(min=10, max=1000)
        ),
    },
    location="query"
)
def generate_students(count):
    students = [
        {
            "first_name": faker_instance.first_name(),
            "last_name": faker_instance.last_name(),
            "email": faker_instance.email(),
            "password": faker_instance.password(),
            "birthday": faker_instance.date_of_birth(minimum_age=18, maximum_age=60)
        }
        for _ in range(count)
    ]

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "students.csv")
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)

    table_html = "<table border='1'><thead><tr>"
    table_html += "".join(f"<th>{key}</th>" for key in students[0].keys())
    table_html += "</tr></thead><tbody>"

    for student in students:
        table_html += "<tr>" + "".join(f"<td>{value}</td>" for value in student.values()) + "</tr>"

    table_html += "</tbody></table>"

    return render_template_string("""
        <h1>List of students</h1>
        <a href="/download_file/students.csv">Download CSV</a>
        <br>
        {{ table_html | safe }}
    """, table_html=table_html)


# http://localhost:5000/download_file/students.csv
@app.route('/download_file/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
