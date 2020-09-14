import unittest
from src.rot13 import rot13

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rot13("test"), "grfg")
        self.assertEqual(rot13("Test"), "Grfg")


if __name__ == '__main__':
    unittest.main()
