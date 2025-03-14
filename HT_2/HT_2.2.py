# Написати код, який прочитає csv-файл і порахує середню вагу студентів
# і середній ріст студентів і повернути це на фронтенд
# csv - use lib


from flask import Flask
import csv

app = Flask(__name__)

@app.route("/calculate_average")
def calculate_average():
    file_path = 'hw_2.csv'

    total_height = 0
    total_weight = 0
    student_count = 0

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            height = float(row[' Height(Inches)'])
            weight = float(row[' Weight(Pounds)'])

            total_height += height
            total_weight += weight
            student_count += 1

    if student_count > 0:
        average_height = total_height / student_count
        average_weight = total_weight / student_count
    else:
        average_height = 0
        average_weight = 0

    return f'Average Height: {average_height:.2f} Inches<br>Average Weight: {average_weight:.2f} Pounds'

if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )

