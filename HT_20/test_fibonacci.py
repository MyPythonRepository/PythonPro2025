import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)
        return self.cache[n]


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci()

    def test_base_cases(self):
        self.assertEqual(self.fib(0), 0)
        self.assertEqual(self.fib(1), 1)

    def test_known_values(self):
        self.assertEqual(self.fib(5), 5)
        self.assertEqual(self.fib(8), 21)
        self.assertEqual(self.fib(10), 55)

    def test_large_value(self):
        self.assertEqual(self.fib(18), 2584)

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            self.fib(-8)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(ValueError):
            self.fib(8.5)
        with self.assertRaises(ValueError):
            self.fib("8")


if __name__ == '__main__':
    unittest.main()
