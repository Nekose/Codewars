def snail(snail_map):
    visited = create_visited_matrix((snail_map))

    #go right
    #if you cant go right, go down
    #if you cant go righ or down, go left
    #if you cant go right,left,or down, go up
    #if you can got up, go right
    pass

def create_visited_matrix(snail_map)->list:
    returnmatrix = []
    for i in snail_map:
        row = []
        for _ in i:
            row.append(False)
        returnmatrix.append(row)
    return returnmatrix

def move(current,direction):
    x,y = current
    if direction == "e":
        return x+1,y
    if direction == "w":
        return x-1,y
    if direction == "n":
        return x, y+1
    if direction == "s":
        return x, y-1

