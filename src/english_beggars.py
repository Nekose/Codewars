def beggars(values, n):
    returnlist = []
    if n == 0:
        return returnlist
    for i in range(n):
        returnlist.append(sum(values[i::n]))
    return returnlist