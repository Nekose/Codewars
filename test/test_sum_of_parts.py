import unittest
from src.sum_of_parts import parts_sums

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(parts_sums([]), [0])
        self.assertEqual(parts_sums([0, 1, 3, 6, 10]), [20, 20, 19, 16, 10, 0])
        self.assertEqual(parts_sums([1, 2, 3, 4, 5, 6]), [21, 20, 18, 15, 11, 6, 0])


if __name__ == '__main__':
    unittest.main()
