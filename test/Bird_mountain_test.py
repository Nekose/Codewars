import unittest
from src.Bird_mountain import *

mountain = [
    "^^^^^^        ",
    " ^^^^^^^^     ",
    "  ^^^^^^^     ",
    "  ^^^^^       ",
    "  ^^^^^^^^^^^ ",
    "  ^^^^^^      ",
    "  ^^^^        "
]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(peak_height(mountain),3)


if __name__ == '__main__':
    unittest.main()
