def parts_sums(ls):
    output = [0]
    sum = 0
    for i in range(len(ls)-1,-1,-1):
        sum += ls[i]
        output.append(sum)
    return [output.pop() for i in range(len(output))]