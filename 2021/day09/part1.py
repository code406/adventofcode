# Find low points on a heightmap. Risk of low point is 1 + its height.
# Sum of risk of all low points is the answer.

def is_low_point(heightmap, x, y, height):
    for i in range(y-1, y+2):
        if i < 0 or i >= len(heightmap): continue
        for j in range(x-1, x+2):
            if j < 0 or j >= len(heightmap[i]) or (i==y and j==x): continue
            if heightmap[i][j] < height: return False
    return True

with open("input.txt", "r") as input:
    heightmap = [list(line.strip()) for line in input]

answer = 0
for y, row in enumerate(heightmap):
    for x, height in enumerate(row):
        if is_low_point(heightmap, x, y, height):
            answer += int(height) + 1
print(answer)