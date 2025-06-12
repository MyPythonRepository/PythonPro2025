# написати свій генератор. Приймає int (кількість слів) а повертає рандомні слова.
# Слова мають бути унікальні, слова мають бути читабельні. Max int = 10_000.


import random
import nltk
from nltk.corpus import words

nltk.download("words", quiet=True)


def generate_unique_words(n):
    max_n = 10_000
    if n > max_n:
        raise ValueError(f"Maximum number of words is {max_n}")

    unique_words = list({w.lower() for w in words.words() if w.isalpha()})
    random.shuffle(unique_words)

    for i in range(n):
        yield unique_words[i]


x = list(generate_unique_words(10_000))
print(len(x))
print(len(set(x)))
