import random
import string


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


print(generate_password())
