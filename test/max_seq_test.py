import unittest
from src.max_seq import max_sequence

class MyTestCase(unittest.TestCase):
    def test_max_seq(self):
        self.assertEqual(max_sequence([]), 0)
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == '__main__':
    unittest.main()
