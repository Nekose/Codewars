import unittest
from src.parseint import parse_int

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(parse_int("one"),1)
        self.assertEqual(parse_int('ten'), 10)
        self.assertEqual(parse_int("one thousand two hundred and forty-one"),1241)
        self.assertEqual(parse_int("one hundred and twelve thousand two hundred and forty-two"),112242)
        self.assertEqual(parse_int("one million"),1000000)
        self.assertEqual(parse_int("zero"),0)

if __name__ == '__main__':
    unittest.main()
