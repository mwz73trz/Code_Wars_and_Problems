import unittest
from calculate_mode import *

class TestCalculateMode(unittest.TestCase):
    "Test for calculate_mode"

    def test_calculate_mode_1(self):
        self.assertEqual(calculate_mode([1, 2, 3, 4, 3]), [3])

    def test_calculate_mode_2(self):
        self.assertEqual(calculate_mode([4.5, 0, 0]), [0])

    def test_calculate_mode_3(self):
        self.assertEqual(calculate_mode([1.5, -1, 1, 1.5]), [1.5])

    def test_calculate_mode_4(self):
        self.assertEqual(calculate_mode([1, 2, 1, 2]), [1, 2])

    def test_calculate_mode_5(self):
        self.assertEqual(calculate_mode([1, 2, 3]), [1, 2, 3])

    def test_calculate_mode_6(self):
        self.assertEqual(calculate_mode(["who", "what", "where", "who"]), ["who"])

if __name__ == '__main__':
    unittest.main()