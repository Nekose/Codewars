import string, math
from decimal import *
def rotation(letter, value):
    startindex = string.ascii_lowercase.index(letter)
    endingindex = startindex + value
    if endingindex > 25:
        endingindex -= 26
    return string.ascii_lowercase[endingindex]

def pi_gibbons(base=10):
    """Gibbons spigot generator of digits of pi in given base."""
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            q, r, t, k, n, l = (base * q, base * (r - n * t), t, k,
                                (base * (3 * q + r)) // t - base * n, l)
        else:
            q, r, t, k, n, l = (q * k, (2 * q + r) * l, t * l, k + 1,
                                (q * (7 * k + 2) + r * l) // (t * l), l + 2)

def return_digit_pi(digit):
    count = 0
    generator = (x for x in pi_gibbons())
    while count < digit:
        print(generator)
    return generator

def rottenpi(string, piposition):
    pass