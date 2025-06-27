# Знайти точку оптимуму для задачі з картинками.
#
# Потоки.
# def fetch_pic(num_pic):
#     url = 'https://picsum.photos/400/600'
#     path = os.path.join(os.getcwd(), 'img')
#     for _ in range(num_pic):
#         random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
#         response = requests.get(url)
#         if response.status_code == 200:
#             with open(f'{path}/{random_name}.jpg', 'wb') as f:
#                 f.write(response.content)


import os
import random
import string
import requests
from multiprocessing.dummy import Pool as ThreadPool
import time


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


workers = 1024
DATA_SIZE = 100

base = DATA_SIZE // workers
remainder = DATA_SIZE % workers
input_data = [base + 1 if i < remainder else base for i in range(workers)]

start = time.time()

with ThreadPool(workers) as pool:
    pool.map(fetch_pic, input_data)

print(f'Elapsed: {round(time.time() - start, 2)}s')
