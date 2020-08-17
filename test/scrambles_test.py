import unittest
from src import Scrambles

class MyTestCase(unittest.TestCase):
    def test_Scrambles(self):
        self.assertEqual(Scrambles.scramble('rkqodlw', 'world'), True)
        self.assertEqual(Scrambles.scramble('cedewaraaossoqqyt', 'codewars'), True)
        self.assertEqual(Scrambles.scramble('katas', 'steak'), False)
        self.assertEqual(Scrambles.scramble('scriptjava', 'javascript'), True)
        self.assertEqual(Scrambles.scramble('scriptingjava', 'javascript'), True)


if __name__ == '__main__':
    unittest.main()
