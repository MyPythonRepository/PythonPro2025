# написати свій генератор. Приймає int (кількість слів) а повертає рандомні слова.
# Слова мають бути унікальні, слова мають бути читабельні. Max int = 10_000.


import random
import nltk
from nltk.corpus import words

nltk.download("words", quiet=True)


def generate_unique_words(n):
    max_n = 10_000
    n = min(n, max_n)
    filtered_words = [w.lower() for w in words.words() if w.isalpha() and len(w) == 8]
    n = min(n, len(filtered_words))
    random.shuffle(filtered_words)
    for i in range(n):
        yield filtered_words[i]


for word in generate_unique_words(5):
    print(word)
