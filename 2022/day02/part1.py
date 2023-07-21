# X/A: Rock (1 point), Y/B: Paper (2 points), Z/C: Scissors (3 points).
# Add W points to what was played. If won, W=6, if draw, W=3, if lost, W=0.

POINTS_PLAYED = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}

def compare(a, b):
    a, b = POINTS_PLAYED[a], POINTS_PLAYED[b]
    if a == b: return 3
    if a == 1 and b == 3: return 6
    if a == 2 and b == 1: return 6
    if a == 3 and b == 2: return 6
    return 0

with open("input.txt", "r") as input:
    data = list(map(str.split, input.read().splitlines()))

print(sum(compare(tup[1], tup[0]) + POINTS_PLAYED[tup[1]] for tup in data))
