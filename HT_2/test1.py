import random
import string


def generate_password():
    length = random.randint(10, 20)

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = random.choices(all_chars, k=length)

    return "".join(password)

print(generate_password())

