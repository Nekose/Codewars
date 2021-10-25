class animal(object):
    def __init__(self, type):
        self.type = type
        if type == "antelope":
            self.eats = ["grass"]
        elif type == "big-fish":
            self.eats = ["little-fish"]
        elif type == "bug":
            self.eats = ["leaves"]
        elif type == "bear":
            self.eats = ["big-fish","bug", "chicken", "cow", "leaves", "sheep"]
        elif type == "chicken":
            self.eats = ["bug"]
        elif type == "cow":
            self.eats = ["grass"]
        elif type == "fox":
            self.eats = ["chicken", "sheep"]
        elif type == "giraffe":
            self.eats = ["leaves"]
        elif type == "lion":
            self.eats = ["antelope", "cow"]
        elif type == "panda":
            self.eats = ["leaves"]
        elif type == 'sheep':
            self.eats = ["grass"]
        else:
            self.eats = []

    def __repr__(self) -> str:
        return self.type


def who_eats_who(zoo):
    zoolist = zoo.split(",")
    classlist = []
    results = [zoo]
    for i in zoolist:
        classlist.append(animal(i))
    done = False
    while done == False and len(classlist) > 1:
        size = len(classlist)
        for pos, val in enumerate(classlist):
            if pos > 0:
                if classlist[pos - 1].type in val.eats:
                    results.append(f"{val.type} eats {classlist[pos - 1].type}")
                    classlist.pop(pos - 1)
                    break
            if pos < size-1:
                if classlist[pos + 1].type in val.eats:
                    results.append(f"{val.type} eats {classlist[pos + 1].type}")
                    classlist.pop(pos + 1)
                    break
        if len(classlist) == size:
            done = True
    results.append(",".join([x.type for x in classlist]))
    return results

print(who_eats_who("chicken,fox,leaves,bug,grass,sheep"))