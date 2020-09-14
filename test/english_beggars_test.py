import unittest
from src.english_beggars import beggars

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(beggars([1, 2, 3, 4, 5], 1), [15])
        self.assertEqual(beggars([1, 2, 3, 4, 5], 2), [9, 6])
        self.assertEqual(beggars([1, 2, 3, 4, 5], 3), [5, 7, 3])
        self.assertEqual(beggars([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5, 0])
        self.assertEqual(beggars([1, 2, 3, 4, 5], 0), [])

if __name__ == '__main__':
    unittest.main()
