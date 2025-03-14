import csv


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

    print(f'Average Height: {average_height:.2f} Inches')
    print(f'Average Weight: {average_weight:.2f} Pounds')

calculate_average()
