# How many seats are occupied after people move all around the plane?
import copy

with open("input.txt", "r") as input:
    plane = [[c for c in l] for l in input.read().splitlines()]

height = len(plane)
width = len(plane[0])

def adjacent(i, j):
    vectors = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    adj = []
    for v in vectors:
        ii = i+v[0]
        jj = j+v[1]
        if 0<=ii<height and 0<=jj<width:
            adj.append(plane[ii][jj])
    return adj

changed = True
while changed == True:
    changed = False
    nu_plane = copy.deepcopy(plane)
    for i in range(height):
        for j in range(width):
            adj_occupied = [a=="#" for a in adjacent(i,j)]
            if plane[i][j]=="L" and not any(adj_occupied):
                nu_plane[i][j] = "#"
                changed = True
            elif plane[i][j]=="#" and sum(adj_occupied)>=4:
                nu_plane[i][j] = "L"
                changed = True
    plane = copy.deepcopy(nu_plane)

print(sum([a=="#" for row in plane for a in row]))
