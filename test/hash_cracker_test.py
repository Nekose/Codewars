import unittest
from src.md5_hash_cracker import crack

class MyTestCase(unittest.TestCase):
    def test_hash_cracher(self):
        self.assertEqual(crack('827ccb0eea8a706c4c34a16891f84e7b'), '12345')
        self.assertEqual(crack('86aa400b65433b608a9db30070ec60cd'), '00078')
        self.assertEqual(crack('4b0cb9685dd1da13cd7d85b3e4de824f'), '31327')
        self.assertEqual(crack('d3eb9a9233e52948740d7eb8c3062d14'), '99999')

if __name__ == '__main__':
    unittest.main()
