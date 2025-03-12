# Створити декоратор для заміру пам'яті


import functools
import psutil
import os

def memory_usage_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss / (1024 * 1024)
        result = func(*args, **kwargs)
        memory_after = process.memory_info().rss / (1024 * 1024)
        print(f"Memory used by {func.__name__}: {memory_after - memory_before:.2f} MB")
        return result

    return wrapper


@memory_usage_decorator
def simple_function():
    data = [i for i in range(10**6)]
    return sum(data)

simple_function()
