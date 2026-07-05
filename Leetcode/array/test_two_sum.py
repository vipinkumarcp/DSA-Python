import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from twoSum import twoSums


class TwoSumTests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(twoSums([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(twoSums([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertEqual(twoSums([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(twoSums([-1, -2, -3, -4, -5], -8), [2, 4])


# class TwosumTest(unittest.TestCase):

#     def test_example_one(self):
#         self.assertEqual(twoSums([2,3,4],5),[2,3])

if __name__ == "__main__":

    unittest.main()
