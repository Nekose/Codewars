def missing(s):
    testlist = sequencer(s)
    if testlist == -1:
        return testlist
    if len(testlist) != testlist[-1] - testlist[0]:
        return -1
    truelist = [x for x in range(testlist[0],testlist[-1] + 1)]
    for test,true in zip(testlist,truelist):
        if test != true:
            return true

def reindexer(lst):
    #TODO allow changing number of digits to next highest (IE, 99 -> 100)
    pass

def sequencer(s):
    for numlist in slicer(s):
        truecount = 0
        for pos,num in enumerate(numlist):
            if pos == 0:
                continue
            if int(num) == int(numlist[pos - 1]) + 1:
                truecount += 1
            else:
                truecount -= 1
        if truecount >= 0:
            return [int(x) for x in numlist]
    return -1

def slicer(s):
    for i in range(1,len(s)//2):
        yield recursive_helper(s,i)

def recursive_helper(s,n):
    returnlist=[]
    return strsplit(s,n,returnlist)


def strsplit(s,n,returnlist):
    if len(s) == 0:
        return returnlist
    strappend, remainder = s[0:n], s[n:]
    if len(remainder) == 0:
        returnlist.append(strappend)
        return strsplit(remainder, n, returnlist)
    elif strappend.count("9") == len(strappend) and remainder[0] == "1" or strappend.count("9") + strappend.count("8") == len(strappend) and remainder[0] == "1":
        if len(returnlist) == 0:
            remainder = s[n:]
            returnlist.append(strappend)
            return strsplit(remainder, n + 1, returnlist)
        elif returnlist[-1].count("9") != len(returnlist[-1]):
            remainder = s[n:]
            returnlist.append(strappend)
            return strsplit(remainder, n+1, returnlist)
    returnlist.append(strappend)
    return strsplit(remainder,n,returnlist)