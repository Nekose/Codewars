import unittest
from src.n_swap_case import swap

class MyTestCase(unittest.TestCase):

    def test_basic_tests(self):
        self.assertEqual(swap('Hello world!', 11), 'heLLO wORLd!')
        self.assertEqual(swap('the quick broWn fox leapt over the fence', 9),
                           'The QUicK BrowN foX LeaPT ovER thE FenCE')
        self.assertEqual(swap('eVerybody likes ice cReam', 85), 'EVErYbODy LiKeS IcE creAM')
        self.assertEqual(swap('gOOd MOrniNg', 7864), 'GooD MorNIng')
        self.assertEqual(swap('how are you today?', 12345), 'HOw are yoU TOdaY?')

    def test_edge_case_tests(self):
        self.assertEqual(swap('the lord of the rings', 0), 'the lord of the rings')
        self.assertEqual(swap('', 11345), '')

if __name__ == '__main__':
    unittest.main()
