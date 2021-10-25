
def duplicate_digits(ndigit):
    total = 0 # in a 1 digit number, duplicates occur 0 times
    for i in range(2,ndigit+1):
        total = (total + (10 ** (i-2)))*9
    #return total
    return total / ((10 ** (ndigit-1)) * 9)

print(duplicate_digits(7))


