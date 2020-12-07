import unittest
from src.prime_gap import gap

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(gap(2, 100, 110), [101, 103])
        self.assertEqual(gap(4, 100, 110), [103, 107])
        self.assertEqual(gap(8, 300, 400), [359, 367])
        self.assertEqual(gap(10, 300, 400), [337, 347])
        self.assertEqual(gap(2, 100, 103), [101, 103])
        self.assertEqual(gap(4, 130, 200), [163, 167])
    def test_impossible(self):
        self.assertEqual(gap(6, 100, 110), None)
        self.assertEqual(gap(2,30000,30012), None)



if __name__ == '__main__':
    unittest.main()
