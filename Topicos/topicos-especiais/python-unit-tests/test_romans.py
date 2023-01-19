import unittest

from src.romans import int_to_roman, roman_to_int


class TestStringMethods(unittest.TestCase):

    def test_basic_roman(self):
        self.assertEqual(int_to_roman(10), 'X')

    def test_basic_int(self):
        self.assertEqual(roman_to_int('X'), 10)

    def test_with_more_len(self):
        self.assertEqual(roman_to_int('II'), 2)

    def test_with_len_three(self):
        self.assertEqual(roman_to_int('XXX'), 30)

    def test_with_one_char(self):
        self.assertEqual(roman_to_int('I'), 1)

    def test_with_len_x(self):
        self.assertEqual(roman_to_int('MMMCMXCIX'), 3999)


if __name__ == '__main__':
    unittest.main()
