# Знайти точку оптимуму для задачі зі списком.
#
# Процеси.
# DATA_SIZE = 10_000_000
# lst = []
#
# def fill_data(n):
#     while n > 0:
#         n -= 1
#         lst.append(random.randint(1, 100))


import random
from multiprocessing import Pool
from time import time

workers = 4
DATA_SIZE = 1_000_000
lst = []


def fill_data(n):
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))
    return lst


if __name__ == '__main__':
    start = time()

    with Pool(workers) as pool:
        input_data = [DATA_SIZE // workers for _ in range(workers)]
        result_parts = pool.map(fill_data, input_data)

    lst = []
    for part in result_parts:
        lst.extend(part)

    print(f'Elapsed: {round(time() - start, 2)}s')
    print(len(lst), lst[:100])
