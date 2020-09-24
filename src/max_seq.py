import itertools
def max_sequence(arr):
    if len(arr) == 0:
        return 0
    maxval = 0
    for i in range(len(arr)):
        generator = itertools.product(arr, repeat=i)
        for list in generator:
            if sum(list) > maxval:
                maxval = sum(list)
    return maxval

def create_all_seqs(arr):
    seqlist = []
    for i in range len(arr):
