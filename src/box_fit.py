def will_fit(present, box):
    present = list(present)
    present.sort(reverse=True)
    box = list(box)
    box.sort(reverse=True)
    maxsize = []
    for val in box:
        maxsize.append(val-2)
    for i in range(3):
        if maxsize[i-1] - present[i-1] < 0:
            return False
    return True

print(will_fit((50, 47, 7), (50, 51, 26)))