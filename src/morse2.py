import itertools
from src.morse_code import decodeMorse
def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bitlist = ["".join(g) for k, g in itertools.groupby(bits)]
    multiplyer = len(min(bitlist,key=len))
    print(multiplyer)
    returnstr = ""
    for element in bitlist:
        for letter in element[::multiplyer]:
            returnstr += letter
    print(returnstr)
    return returnstr.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')


def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')

print(decodeMorse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))