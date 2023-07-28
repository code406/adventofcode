# count the number of trees that are visible from outside the grid when
# looking directly along a row or column. Values in input are tree heights

with open("input.txt", "r") as input:
    grid = [
        [(f"{x},{y}", int(char)) for x, char in enumerate(line)]
        for y, line in enumerate(input.read().splitlines())
    ]

visible_trees = set()
for _ in range(4):
    for row in grid:
        tallest_seen = -1
        for tree in row:
            if tree[1] > tallest_seen:
                visible_trees.add(tree[0])
                tallest_seen = tree[1]
    grid = [*zip(*grid[::-1])] # rotate 90deg

print(len(visible_trees))
