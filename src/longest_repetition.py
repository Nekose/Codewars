def longest_repetition(chars):
    if len(chars) == 0:
        return "",0
    for pos,element in enumerate(chars):
        if pos == 0:
            currentletter = element
            currentcount = 1
            highcount = 1
            highletter = element
            continue
        if element == currentletter:
            currentcount += 1
        else:
            currentcount = 1
            currentletter = element
        if currentcount > highcount:
            highcount = currentcount
            highletter = element
    return highletter,highcount