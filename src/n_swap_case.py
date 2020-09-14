import itertools
def swap(s,n):
    binary = bin(n)[2:]
    returnstr = ""
    cycle = itertools.cycle(binary)
    for letter in s:
        if letter.isalpha():
            if next(cycle) == "1":
                returnstr += letter.swapcase()
            else:
                returnstr += letter
        else:
            returnstr += letter
    return returnstr