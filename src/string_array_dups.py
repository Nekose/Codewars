def dup(arry):
    returnlist=[]
    for word in arry:
        strippedword = ""
        for pos,letter in enumerate(word):
            if pos == 0:
                strippedword += letter
            elif word[pos-1] == letter:
                continue
            else:
                strippedword += letter
        returnlist.append(strippedword)
    return returnlist