class Warrior(object):

    def __init__(self):
        self.level = 1
        self.ranklist = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.rank = self.ranklist[0]
        self.experience = 100
        self.achievments = []

    def update_level(self):
        if self.level >= 100:
            self.level = 100
        self.level = self.experience // 100
        self.rankup()

    def rankup(self):
        rank = self.determine_rank_number(self.level)
        if rank > 10:
            rank = 10
        self.rank = self.ranklist[rank]

    def determine_rank_number(self,level):
        if level == 100:
            return 10
        else:
            return level // 10


    def battle(self,enemy_level):
        rank_diff = self.determine_rank_number(self.level) - self.determine_rank_number(enemy_level)
        level_diff = self.level - enemy_level
        if enemy_level < 1 or enemy_level > 100:
            return "Invalid level"
        if self.level == enemy_level:
            self.experience += 10
        elif self.level - enemy_level == 1:
            self.experience += 5
        elif self.level - enemy_level >= 2:
            pass
        else:
            if rank_diff < 0 and level_diff < -4:
                return "You've been defeated"
            else:
                self.experience += 20 * level_diff * level_diff
        self.update_level()
        if level_diff >= 2:
            return "Easy fight"
        elif level_diff > 0:
            return "A good fight"
        else:
            return "An intense fight"


    def training(self, requirements):
        description, exp, min_level = requirements
        if self.level >= min_level:
            self.achievments.append(description)
            self.experience += exp
            self.update_level()
            return description
        else:
            return "Not strong enough"

peter = Warrior()
peter.experience = 600
peter.update_level()
print(peter.level)
print(peter.rank)
print(peter.battle(2))
print(peter.experience)
print(peter.level)
print(peter.rank)
print(peter.training(["kicked butt",9000,8]))
print(peter.experience)