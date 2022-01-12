# Line format: x1,y1 -> x2,y2 (vert/horiz/diag)
# At how many points do at least 2 lines cross?

with open("input.txt", "r") as input:
    lines = [list(map(int, ((",").join(l.split(" -> "))).split(",")))
             for l in input.read().splitlines()]

boundx = max(max(l[0], l[2]) for l in lines)
boundy = max(max(l[1], l[3]) for l in lines)
diagram = [[0 for _ in range(boundx+1)] for _ in range(boundy+1)]
for x1,y1,x2,y2 in lines:
    if y1 == y2: # horizontal
        for x in range(min(x1, x2), max(x1, x2)+1): diagram[y1][x] += 1
    elif x1 == x2: # vertical
        for y in range(min(y1, y2), max(y1, y2)+1): diagram[y][x1] += 1
    elif x1 < x2 and y1 < y2: # diagonal right down
        for i in range(x2-x1+1): diagram[y1+i][x1+i] += 1
    elif x1 > x2 and y1 < y2: # diagonal left down
        for i in range(x1-x2+1): diagram[y1+i][x1-i] += 1
    elif x1 < x2 and y1 > y2: # diagonal right up
        for i in range(x2-x1+1): diagram[y1-i][x1+i] += 1
    elif x1 > x2 and y1 > y2: # diagonal left up
        for i in range(x1-x2+1): diagram[y1-i][x1-i] += 1

print(len([c for line in diagram for c in line if c > 1]))