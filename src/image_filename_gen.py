import random

def generateName():
    randomname = 'AAAAAA'
    while not photoManager.nameExists(randomname):
        randomname = "".join(random.choices([chr(x) for x in range(64,91)]+[chr(x) for x in range(97,123)],k=6))
    return randomname

generateName()