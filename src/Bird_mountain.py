def peak_height(mountain):
    updatemap = convert_matrix(mountain)
    flatmap = True
    for row in updatemap:
        for col in row:
            if col == "^":
                flatmap = False
    if flatmap == True:
        return 0
    currentheight = 0
    done = False
    while done == False:
        updatemap, done = outline_mountains(updatemap, currentheight)
        currentheight += 1
    return currentheight


def convert_matrix(arry):
    returnarray = []
    for row in arry:
        returnrow = []
        for collumn in row:
            if collumn == " ":
                returnrow.append(0)
            else:
                returnrow.append(collumn)
        returnarray.append(returnrow)
    return returnarray


def check_nsew(map, row, col):
    # check north
    if row == 0:
        north = 0
    else:
        north = map[row - 1][col]
    # check south
    if row == len(map) - 1:
        south = 0
    else:
        south = map[row + 1][col]
    # check east
    if col == len(map[0]) - 1:
        east = 0
    else:
        east = map[row][col + 1]
    # check west
    if col == 0:
        west = 0
    else:
        west = map[row][col - 1]
    print(north,south,east,west)
    return (north, south, east, west)


def outline_mountains(map, currentheight):
    done = True
    returnmap = []
    for rowpos, val1 in enumerate(map):
        returnrow = []
        for colpos, val2 in enumerate(val1):
            if val2 == "^" and currentheight in check_nsew(map, rowpos, colpos):
                returnrow.append(currentheight + 1)
            else:
                returnrow.append(val2)
        if "^" in returnrow:
            done = False
        returnmap.append(returnrow)
    return returnmap, done