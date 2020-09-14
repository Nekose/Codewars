import unittest
from src.longest_repetition import longest_repetition


class MyTestCase(unittest.TestCase):
    def test_longest(self):
        self.assertEqual(longest_repetition('aaaaa'),('a',5))
        self.assertEqual(longest_repetition('abc'), ('a', 1))
        self.assertEqual(longest_repetition('aaaaab'), ('a', 5))
        self.assertEqual(longest_repetition('abbbbb'), ('b', 5))
        self.assertEqual(longest_repetition(''), ('', 0))
if __name__ == '__main__':
    unittest.main()
