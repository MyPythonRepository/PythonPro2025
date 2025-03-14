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

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = random.choices(all_chars, k=length)

    return "".join(password)


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )

