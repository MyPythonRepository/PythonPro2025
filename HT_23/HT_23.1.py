# custom map (iterator), приймає dict і приймає 2 функції.
# першу фунцію застосовуємо до ключів а другу до значень.
# map(dict, func1, funct2)
# (func1(key), func2(value))


dict1 = {"a": 1, "b": 2, "C": 80}


def map_dict(my_dict, func1, func2):
    return {func1(k): func2(v) for k, v in my_dict.items()}


new_dict = map_dict(dict1, str.upper, lambda x: x * 20)
print(new_dict)
