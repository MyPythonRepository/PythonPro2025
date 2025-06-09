# custom map (iterator), приймає dict і приймає 2 функції.
# першу фунцію застосовуємо до ключів а другу до значень.
# map(dict, func1, funct2)
# (func1(key), func2(value))


dict1 = {"a": 1, "b": 2, "C": 80}


def map_dict(my_dict, func1, func2):
    for k, v in my_dict.items():
        yield func1(k), func2(v)

new_iter = map_dict(dict1, str.upper, lambda x: x * 20)

new_dict = dict(new_iter)
print(new_dict)
