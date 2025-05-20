import unittest


def formatted_name(first_name, last_name, middle_name=''):
    names = [first_name, middle_name, last_name]
    full_name = ' '.join(i for i in names if i)
    return full_name.title()


class TestFormattedName(unittest.TestCase):
    def test_without_middle_name(self):
        self.assertEqual(formatted_name("iryna", "s"), "Iryna S")

    def test_with_middle_name(self):
        self.assertEqual(formatted_name("iryna", "sh", "o"), "Iryna O Sh")

    def test_with_empty_strings(self):
        self.assertEqual(formatted_name("", "s"), "S")
        self.assertEqual(formatted_name("iryna", ""), "Iryna")
        self.assertEqual(formatted_name("", ""), "")

    def test_capitalization(self):
        self.assertEqual(formatted_name("IRYNA", "SH"), "Iryna Sh")
        self.assertEqual(formatted_name("IrYnA", "ShA"), "Iryna Sha")


if __name__ == '__main__':
    unittest.main()
