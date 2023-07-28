# Rope is H (head) and T (tail). If head moves and they dont touch
# tail moves towards head. Count all positions visited by tail

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

hx, hy = 0, 0
tx, ty = 0, 0
visited = set()
for line in lines:
    for _ in range(int(line[2:])):
        if   line[0] == "R": hx += 1
        elif line[0] == "L": hx -= 1
        elif line[0] == "U": hy += 1
        elif line[0] == "D": hy -= 1
        
        if abs(hx - tx) <= 1 and abs(hy - ty) <= 1: continue
        elif hx > tx and hy > ty: tx += 1; ty += 1
        elif hx > tx and hy < ty: tx += 1; ty -= 1
        elif hx < tx and hy > ty: tx -= 1; ty += 1
        elif hx < tx and hy < ty: tx -= 1; ty -= 1
        elif hx > tx: tx += 1
        elif hx < tx: tx -= 1
        elif hy > ty: ty += 1
        elif hy < ty: ty -= 1

        visited.add((tx, ty))

print(len(visited))
