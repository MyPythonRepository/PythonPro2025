# Реалізувати LFU алгоритм для кешування.
# За базу берем існуючий декоратор.
# Написати для фетчування юерелів.
# Додати можливість указати максимум елементів в кеші.


import functools
import requests
from collections import OrderedDict


def lfu_cache(max_limit=64):
    def internal(f):
        cache = OrderedDict()
        frequencies = OrderedDict()

        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))

            if cache_key in cache:
                frequencies[cache_key] += 1
                cache.move_to_end(cache_key)
                return cache[cache_key]

            result = f(*args, **kwargs)

            if len(cache) >= max_limit:
                lfu_key = min(frequencies, key=frequencies.get)
                cache.pop(lfu_key)
                frequencies.pop(lfu_key)

            cache[cache_key] = result
            frequencies[cache_key] = 1
            cache.move_to_end(cache_key)

            return result

        return deco
    return internal


@lfu_cache(max_limit=5)
def fetch_url(url, first_n=100):
    """Fetch a given URL"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content
