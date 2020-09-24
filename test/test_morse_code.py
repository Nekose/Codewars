from src.morse_code import decodeMorse
from unittest import TestCase


class Test_decodeMorse(TestCase):
    def test_decode_morse(self):
        self.assertEqual(decodeMorse(".... . -.--   .--- ..- -.. ."),"HEY JUDE")
        self.assertEqual(decodeMorse("      .... . -.--   .--- ..- -.. .    "), "HEY JUDE")
        self.assertEqual(decodeMorse("...---..."), "SOS")
        self.assertEqual(decodeMorse(".--. . - . .-."), "PETER")

