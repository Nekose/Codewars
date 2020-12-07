def find_unknown_number(x,y,z):
    n = 0
    while n % 3 != x or n % 5 != y or n % 7 !=z:
        n += 1
    return n

print(find_unknown_number(2,3,2))