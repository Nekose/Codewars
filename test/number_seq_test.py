import unittest
from src.number_seq import missing


class MyTestCase(unittest.TestCase):
    def testSequence(self):
        self.assertEqual(missing("123567"), 4)
        self.assertEqual(missing("899091939495"), 92)
        self.assertEqual(missing("9899101102"), 100)
        self.assertEqual(missing("599600601602"), -1)
        self.assertEqual(missing("8990919395"), -1)
        self.assertEqual(missing("998999100010011003"), 1002)
        self.assertEqual(missing("99991000110002"), 10000)
        self.assertEqual(missing("979899100101102"), -1)
        self.assertEqual(missing("900001900002900004900005900006"), 900003)


if __name__ == '__main__':
    unittest.main()
