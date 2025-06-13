# custom map (iterator), приймає dict і приймає 2 функції.
# першу фунцію застосовуємо до ключів а другу до значень.
# map(dict, func1, funct2)
# (func1(key), func2(value))


dict1 = {"a": 1, "b": 2, "C": 80}


class MapDict:
    def __init__(self, my_dict, func1, func2):
        self._items = list(my_dict.items())
        self.func1 = func1
        self.func2 = func2
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self._items):
            raise StopIteration
        key, value = self._items[self.index]
        self.index += 1
        return (self.func1(key), self.func2(value))


new_iter = MapDict(dict1, str.upper, lambda x: x * 20)

new_dict = dict(new_iter)
print(new_dict)
