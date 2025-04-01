from decimal import Decimal


class FRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.current_value = Decimal(str(start))
        self.stop = Decimal(str(stop))
        self.step = Decimal(str(step))

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current_value >= self.stop) or (self.step < 0 and self.current_value <= self.stop):
            raise StopIteration
        value = self.current_value
        self.current_value += self.step
        return float(value)


for i in FRange(1, 100, 3.5):
    print(i)


assert (list(FRange(5)) == [0, 1, 2, 3, 4])
assert (list(FRange(2, 5)) == [2, 3, 4])
assert (list(FRange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(FRange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(FRange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(FRange(1, 5)) == [1, 2, 3, 4])
assert (list(FRange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(FRange(0, 0)) == [])
assert (list(FRange(100, 0)) == [])

print('SUCCESS!')
