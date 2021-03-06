import unittest
from src.sha1_hash_cracker import password_cracker,password_cracker2

hashdict = {}
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(password_cracker("86F7E437FAA5A7FCE15D1DDCB9EAEAEA377667B8".lower()),'a')
        self.assertEqual(password_cracker('e6fb06210fafc02fd7479ddbed2d042cc3a5155e'), 'code')
        self.assertEqual(password_cracker('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'), 'test')
        self.assertEqual(password_cracker('DF51E37C269AA94D38F93E537BF6E2020B21406C'.lower()), 'aaaaa')
        self.assertEqual(password_cracker('A2B7CADDBC353BD7D7ACE2067B8C4E34DB2097A3'.lower()), 'zzzzz')


    def test_cracker2(self):
        self.assertEqual(password_cracker2("86F7E437FAA5A7FCE15D1DDCB9EAEAEA377667B8".lower()), 'a')
        self.assertEqual(password_cracker2('e6fb06210fafc02fd7479ddbed2d042cc3a5155e'), 'code')
        self.assertEqual(password_cracker2('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'), 'test')
        self.assertEqual(password_cracker2('DF51E37C269AA94D38F93E537BF6E2020B21406C'.lower()), 'aaaaa')
        self.assertEqual(password_cracker2('A2B7CADDBC353BD7D7ACE2067B8C4E34DB2097A3'.lower()), 'zzzzz')


if __name__ == '__main__':
    unittest.main()
