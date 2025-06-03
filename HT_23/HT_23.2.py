# написати свій генератор. Приймає int (кількість слів) а повертає рандомні слова.
# Слова мають бути унікальні, слова мають бути читабельні. Max int = 10_000.


import random
import nltk
from nltk.corpus import words

nltk.download("words", quiet=True)


def generate_unique_words(n):
    return random.sample([w.lower() for w in words.words() if w.isalpha() and 8 <= len(w) <= 8], n)


print(generate_unique_words(5))
