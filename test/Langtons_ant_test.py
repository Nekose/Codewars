import unittest
from src.Langtons_ant import ant, update_grid, step

class MyTestCase(unittest.TestCase):
    def test_update_grid(self):
        self.grid = [[1,1,1],[0,0,0],[1,1,1]]
        self.assertEqual(update_grid(self.grid,1,1),[[1, 1, 1], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(update_grid(self.grid, 0, 0), [[0, 1, 1], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(update_grid(self.grid, 0, 0), [[1, 1, 1], [0, 1, 0], [1, 1, 1]])


if __name__ == '__main__':
    unittest.main()
