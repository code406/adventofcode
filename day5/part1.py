# What is the highest seat ID on a boarding pass?
with open("input.txt", "r") as input:
    lines = input.read().splitlines()

taken = []
for l in lines:
    row = int(l[:-3].replace("B","1").replace("F","0"), 2)
    col = int(l[-3:].replace("R","1").replace("L","0"), 2)
    taken.append(row * 8 + col)

print(max(taken))
