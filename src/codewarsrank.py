class User(object):
    def __init__(self) -> None:
        super().__init__()
        self.rank = -8
        self.progress = 0
        self.scale = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def inc_progress(self,difficulty):
        if difficulty > 8 or difficulty < -8:
            raise ArithmeticError
        if self.rank == 8:
            return
        adjustedrank = self.scale.index(self.rank)
        adjusteddifficuluty = self.scale.index(difficulty)
        difference = adjusteddifficuluty - adjustedrank
        if difference == 0:
            self.progress += 3
        elif difference == -1:
            self.progress += 1
        elif difference <= -2:
            pass
        else:
            self.progress += 10 * (difference * difference)
        self.rankup()
    def rankup(self):
        if self.progress < 100:
            return
        else:
            rankup = self.progress // 100
            self.progress %= 100
            newrank = self.scale.index(self.rank) + rankup
            if newrank > 15:
                newrank = 15
            self.rank = self.scale[newrank]
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0

peter = User()
print(peter.rank)
peter.inc_progress(-7)
print(peter.rank)
print(peter.progress)
peter.inc_progress(-5)
print(peter.rank)
print(peter.progress)