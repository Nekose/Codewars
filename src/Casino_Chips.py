def solve(arr):
    currentstack = stack(arr)
    chipcount = 0
    print(currentstack.most_common_chiptype())
    while len(currentstack.chip_types_remaining()) > 1:
        currentchip = currentstack.stacklist.pop()
        chipcount += 1
        for pos,chip in enumerate(currentstack.stacklist):
            if currentchip != chip:
                currentstack.stacklist.pop(pos)
                chipcount += 1
    return chipcount // 2

class stack(object):
    def __init__(self,stacklist):
        self.stacklist = []
        for i in range (len(stacklist)):
            for _ in range(stacklist[i]):
                self.stacklist.append(chip(i))

    def chip_types_remaining(self):
        chiptypelist = {chip.chiptype for chip in self.stacklist}
        return chiptypelist

    def most_common_chiptype(self):
        chiptypedict = {}
        for element in self.stacklist:
            if element.chiptype in chiptypedict:
                chiptypedict[element.chiptype] += 1
            else:
                chiptypedict[element.chiptype] = 1
        return max(chiptypedict, key= lambda )


class chip(object):
    def __init__(self,type) -> None:
        self.chiptype = type
        super().__init__()

    def __repr__(self):
        return f"a {self.chiptype} chip"

    def __eq__(self, other):
        if self.chiptype == other.chiptype:
            return True
        else:
            return False

print(solve([1,2,1]))