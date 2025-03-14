from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/calculate_average")
def calculate_average():
    file_path = 'hw_2.csv'

    df = pd.read_csv(file_path)

    average_height = df[' Height(Inches)'].mean()
    average_weight = df[' Weight(Pounds)'].mean()

    return f'Average Height: {average_height:.2f} Inches<br>Average Weight: {average_weight:.2f} Pounds'

if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )