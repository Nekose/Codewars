import unittest
from src.string_array_dups import dup


class MyTestCase(unittest.TestCase):
    def test_dups(self):
        self.assertEqual(dup(["ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"]),
                           ['codewars', 'picaniny', 'hubububo'])
        self.assertEqual(dup(["abracadabra", "allottee", "assessee"]), ['abracadabra', 'alote', 'asese'])
        self.assertEqual(dup(["kelless", "keenness"]), ['keles', 'kenes'])
        self.assertEqual(dup(["Woolloomooloo", "flooddoorroommoonlighters", "chuchchi"]),
                           ['Wolomolo', 'flodoromonlighters', 'chuchchi'])
        self.assertEqual(dup(["adanac", "soonness", "toolless", "ppellee"]), ['adanac', 'sones', 'toles', 'pele'])
        self.assertEqual(dup(["callalloo", "feelless", "heelless"]), ['calalo', 'feles', 'heles'])
        self.assertEqual(dup(["putteellinen", "keenness"]), ['putelinen', 'kenes'])
        self.assertEqual(dup(["kelless", "voorraaddoosspullen", "achcha"]), ['keles', 'voradospulen', 'achcha'])


if __name__ == '__main__':
    unittest.main()
