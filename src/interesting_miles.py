def is_interesting(number:int, awesome_phrases:list) -> int:
    if check_is_interesting(number,awesome_phrases):
        return 2
    if check_is_interesting(number+1,awesome_phrases) or check_is_interesting(number+2,awesome_phrases):
        return 1
    else:
        return 0

def check_is_interesting(number,awesome_phrases):
    if number < 100:
        return False
    if is_awesome_phrase(number,awesome_phrases):
        return True
    elif is_in_ascending_order(number):
        return True
    elif is_in_descending_order(number):
        return True
    elif is_all_zero(number):
        return True
    elif is_all_same(number):
        return True
    elif is_palindrome(number):
        return True
    else:
        return False


def is_awesome_phrase(number:int, awesome_phrases:list)-> bool:
    if number in awesome_phrases:
        return True
    return False

def is_all_zero(number:int) ->bool:
    strnum = str(number)
    nonzero = strnum.strip("0")
    if len(nonzero) == 1:
        return True
    return False

def is_all_same(number:int) -> bool:
    strnum = str(number)
    if strnum.count(strnum[0]) == len(strnum):
        return True
    return False

def is_in_ascending_order(number:int) -> bool:
    numstr = str(number)
    listnum = list(numstr)
    for pos,val in enumerate(listnum):
        if pos == 0:
            continue
        if int(val) == 0 and int(listnum[pos-1]) == 9:
            continue
        if int(val) == int(listnum[pos-1]) + 1 and int(listnum[pos-1]) != 0:
            continue
        else:
            return False
    return True

def is_in_descending_order(number:int) -> bool:
    numstr = str(number)
    listnum = list(numstr)
    for pos,val in enumerate(listnum):
        if pos == 0:
            continue
        if int(val) == int(listnum[pos-1]) -1:
            continue
        else:
            return False
    return True

def is_palindrome(number:int) -> bool:
    strnum = str(number)
    numdigits = len(strnum)
    if numdigits % 2 == 0:
        leftstop = int((numdigits)/2)
        rightstart = leftstop
        leftside = strnum[:leftstop]
        rightside = strnum[rightstart:]
    else:
        leftstop = int((numdigits - 1) / 2)
        rightstart = int(leftstop + 1)
        leftside = strnum[:leftstop]
        rightside = strnum[rightstart:]
    flippedright = rightside[::-1]
    if leftside == flippedright:
        return True
    else:
        return False
