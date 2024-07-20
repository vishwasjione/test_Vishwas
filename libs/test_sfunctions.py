import unittest
from sfunctions import add_two_numbers, multiply_two_numbers

class TestSFunctions(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(5, 7), 12)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(-5, -7), -12)

    def test_multiply_two_numbers(self):
        self.assertEqual(multiply_two_numbers(3, 7), 21)
        self.assertEqual(multiply_two_numbers(-1, 1), -1)
        self.assertEqual(multiply_two_numbers(-2, -4), 8)
        self.assertEqual(multiply_two_numbers(0, 5), 0)

if __name__ == '__main__':
    unittest.main()