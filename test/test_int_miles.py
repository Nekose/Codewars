import unittest
from src import interesting_miles


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.awesome_phrases = [1337, 80085]
        self.awesome_phrases2 = []

    def test_is_awesome_phrase(self):
        self.assertEqual(True, interesting_miles.is_awesome_phrase(1337,self.awesome_phrases))
        self.assertEqual(False, interesting_miles.is_awesome_phrase(4343, self.awesome_phrases))
        self.assertEqual(False, interesting_miles.is_awesome_phrase(4343, self.awesome_phrases2))

    def test_all_zeroes(self):
        self.assertEqual(True,interesting_miles.is_all_zero(100000))
        self.assertEqual(False, interesting_miles.is_all_zero(110000))
        self.assertEqual(False, interesting_miles.is_all_zero(1010000))
    def test_palindrome(self):
        self.assertEqual(True,interesting_miles.is_palindrome(12021))
        self.assertEqual(True, interesting_miles.is_palindrome(1221))
        self.assertEqual(True, interesting_miles.is_palindrome(101))
        self.assertEqual(True, interesting_miles.is_palindrome(1111111111111111))
        self.assertEqual(True, interesting_miles.is_palindrome(1110111))
        self.assertEqual(False, interesting_miles.is_palindrome(1100))
        self.assertEqual(False, interesting_miles.is_palindrome('00000110000'))
    def test_allsame(self):
        self.assertEqual(True, interesting_miles.is_all_same(111111))
        self.assertEqual(False, interesting_miles.is_all_same(1111011))
        self.assertEqual(False, interesting_miles.is_all_same(1010101010))
        self.assertEqual(True, interesting_miles.is_all_same(99999999))
    def test_in_ascending_order(self):
        self.assertEqual(True, interesting_miles.is_in_ascending_order(123456789))
        self.assertEqual(False, interesting_miles.is_in_ascending_order(54321))
        self.assertEqual(False, interesting_miles.is_in_ascending_order(1479))
        self.assertEqual(True, interesting_miles.is_in_ascending_order(7890))
        self.assertEqual(False, interesting_miles.is_in_ascending_order(78901))
        self.assertEqual(False, interesting_miles.is_in_ascending_order(1111111))
        self.assertEqual(True, interesting_miles.is_in_ascending_order(4567))
    def test_in_descending_order(self):
        self.assertEqual(True, interesting_miles.is_in_descending_order(54321))
        self.assertEqual(True, interesting_miles.is_in_descending_order(98765))
        self.assertEqual(False, interesting_miles.is_in_descending_order(12345))
        self.assertEqual(False, interesting_miles.is_in_descending_order(11111))
    def test_is_interesting(self):
        self.assertEqual(2,interesting_miles.is_interesting(11111,self.awesome_phrases))
        self.assertEqual(1, interesting_miles.is_interesting(11110, self.awesome_phrases))
        self.assertEqual(1, interesting_miles.is_interesting(11109, self.awesome_phrases))
        self.assertEqual(0, interesting_miles.is_interesting(11108, self.awesome_phrases))
        self.assertEqual(2, interesting_miles.is_interesting(1337, self.awesome_phrases))
        self.assertEqual(1, interesting_miles.is_interesting(1336, self.awesome_phrases))
        self.assertEqual(1, interesting_miles.is_interesting(1335, self.awesome_phrases))
        self.assertEqual(0, interesting_miles.is_interesting(1334, self.awesome_phrases))

if __name__ == '__main__':
    unittest.main()
