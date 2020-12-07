def gap(g, m, n):
    primelist = ((i,is_prime(i)) for i in range(m,n+1))
    gapstart = m
    for (val,isprime) in primelist:
        if isprime is True:
            if val - gapstart == g:
                return [gapstart,val]
            else:
                gapstart = val
    return None

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True