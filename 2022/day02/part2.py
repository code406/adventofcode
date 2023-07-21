# X/A: Rock (1 point), Y/B: Paper (2 points), Z/C: Scissors (3 points).
# Add W points to what was played. If won, W=6, if draw, W=3, if lost, W=0.

POINTS_PLAYED = {'A': 1, 'B': 2, 'C': 3}
HOW_TO_WIN = {'A': 'B', 'B': 'C', 'C': 'A'}
HOW_TO_LOSE = {'A': 'C', 'B': 'A', 'C': 'B'}

with open("input.txt", "r") as input:
    data = list(map(str.split, input.read().splitlines()))

s = 0
for tup in data:
    if tup[1] == 'X': s += POINTS_PLAYED[HOW_TO_LOSE[tup[0]]]
    elif tup[1] == 'Z': s += 6+POINTS_PLAYED[HOW_TO_WIN[tup[0]]]
    else: s += 3+POINTS_PLAYED[tup[0]]

print(s)
