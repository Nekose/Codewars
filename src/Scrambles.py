def scramble(s1: str, s2: str) -> bool:
    """
    :param s1:
    A scrambled sequence of letters
    :param s2:
    A key word, to be found in the scramble
    :return:
    If s2 can be found within s1, return True. Else return False
    """
    scrambledict = {}
    for letter in s1:
        if letter in scrambledict:
            scrambledict[letter] += 1
        else:
            scrambledict[letter] = 1
    try:
        for letter in s2:
            scrambledict[letter] -= 1
            if scrambledict[letter] < 0:
                return False
    except KeyError:
        return False
    return True