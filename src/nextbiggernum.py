import itertools

def next_bigger(n):
    print(n)
    for i in range(len(str(n))-1,0,-1):
        strlist = [char for char in str(n)]
        testval = strlist.pop(i)
        strlist.append(testval)
        testnum = int("".join(strlist))
        if testnum > n:
            return testnum
    return -1

print(next_bigger(12365))