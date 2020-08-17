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
    worddict = {}
    for letter in s1:
        if letter in scrambledict:
            scrambledict[letter] += 1
        else:
            scrambledict[letter] = 1
    for letter in s2:
        if letter in worddict:
            worddict[letter] += 1
        else:
            worddict[letter] = 1
    try:
        for element in worddict:
            lettercount = worddict[element]
            if lettercount > scrambledict[element]:
                return False
        return True
    except KeyError:
        return False
