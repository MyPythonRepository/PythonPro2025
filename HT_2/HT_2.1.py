# Написати в’ю "/generate_password" – вона генерує пароль наступним чином –
# пароль маю бути від 10 до 20 символів рандомно,
# мають бути великі і маленькі символи + пароль має містити
# хоча б один з цих елементів : string, ascii_lowercase, ascii_uppercase,
# int, special symbols і ця в’ю має повернути цей рандомний пароль
# (повернути це на фронтенд).


from flask import Flask
import random
import string

app = Flask(__name__)


@app.route("/generate_password")
def generate_password():
    length = random.randint(10, 20)

    upper_char = random.choice(string.ascii_uppercase)
    lower_char = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special_symbol = random.choice(string.punctuation)

    rest_of_length = length - 4
    add_chars = string.ascii_letters + string.digits + string.punctuation
    random_chars = random.choices(add_chars, k=rest_of_length)

    password = [upper_char, lower_char, digit, special_symbol] + random_chars
    random.shuffle(password)

    return "".join(password)


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
