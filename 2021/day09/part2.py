# Find low points & then find basins (all points that flow downward to a 
# single low point, excluding 9s). Mult of sizes of 3 largest basins.

def is_low_point(heightmap, height, adjacents):
    for (i, j) in adjacents:
        if heightmap[j][i] < height: return False
    return True

def adjacents(heightmap, x, y):
    for (i, j) in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]:
        if j < 0 or j >= len(heightmap) or i < 0 or i >= len(heightmap[j]): continue
        yield (i, j)

def build_basin(heightmap, x, y, basin):
    basin.append((x, y))
    for (i, j) in adjacents(heightmap, x, y):
        if heightmap[j][i] > heightmap[y][x] and heightmap[j][i] != '9':
            build_basin(heightmap, i, j, basin)
    return basin

with open("input.txt", "r") as input:
    heightmap = [list(line.strip()) for line in input]

low_points = []
for y, row in enumerate(heightmap):
    for x, height in enumerate(row):
        if is_low_point(heightmap, height, adjacents(heightmap, x, y)):
            low_points.append((x, y))

sizes = []
for (x, y) in low_points:
    sizes.append(len(list(set(build_basin(heightmap, x, y, [])))))
sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])