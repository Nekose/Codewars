import itertools
def solve(arr):
    returnlist = []
    for i in range(1,len(arr)+1):
        combos=[]
        for val in itertools.combinations(arr,i):
            combos.append(val)
        returnlist.append(combos)
    for pos,val in enumerate(returnlist):
        for i in range(len(val)):
            returnlist[pos][i] = sum(returnlist[pos][i])
    returnlist = itertools.chain.from_iterable(returnlist)
    returnnum = 1
    while returnnum in returnlist:
        returnnum +=1
    return returnnum

print(solve([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))