import unittest
from src.snail import *


class snailmap(unittest.TestCase):
    array1 = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    expectedvisited1 = [[False, False, False],
             [False, False, False],
             [False, False, False]]
    array2 = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    expected2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def test_array1(self):
        self.assertEqual(snail(self.array1), self.expected1)
    def test_array2(self):
        self.assertEqual(snail(self.array2), self.expected2)
    def test_create_visited_matrix(self):
        self.assertEqual(create_visited_matrix(self.array1),self.expectedvisited1)



if __name__ == '__main__':
    unittest.main()
