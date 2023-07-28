# scenic score: product of tree's viewing distances in every direction
# viewing distance is the number of trees that can be seen
from collections import defaultdict

with open("input.txt", "r") as input:
    grid = [
        [(f"{x},{y}", int(char)) for x, char in enumerate(line)]
        for y, line in enumerate(input.read().splitlines())
    ]

scores = defaultdict(list)
for _ in range(4):
    for row in grid:
        for i, tree in enumerate(row):
            num_trees = 0
            for t in row[i+1:]:
                num_trees += 1
                if t[1] >= tree[1]: break
            scores[tree[0]].append(num_trees)
    grid = [*zip(*grid[::-1])] # rotate 90deg

print(max([v[0]*v[1]*v[2]*v[3] for v in scores.values()]))
