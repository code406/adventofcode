# 10x10 octopus energy grid. Energy += 1. If >9, flash, increasing adjacents
# energy by 1. If adjacents >9, they flash. After flashing, they go back to 0.

def adjacents(grid, x, y):
    for j in range(y-1, y+2):
        if j < 0 or j >= len(grid): continue
        for i in range(x-1, x+2):
            if i < 0 or i >= len(grid[j]) or (i==x and j==y): continue
            yield (i, j)

def flash(grid, x, y, flashed):
    if (x, y) in flashed: return
    flashed.append((x, y))
    for i, j in adjacents(grid, x, y):
        grid[j][i] += 1
        if grid[j][i] > 9: flash(grid, i, j, flashed)

with open("input.txt", "r") as input:
    grid = [list(map(int, list(line))) for line in input.read().splitlines()]

flash_count = 0
for step in range(100):
    flashed = []
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            grid[j][i] += 1
            if grid[j][i] > 9: flash(grid, i, j, flashed)
    for i, j in flashed: grid[j][i] = 0
    flash_count += len(flashed)
print(flash_count)