# Rope is H (head) and T (tail). If head moves and they dont touch
# tail moves towards head. Count all positions visited by tail

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

# part2: now there are 10 points in the rope, not 2
rope = [[0, 0] for _ in range(10)]
visited = set()
for line in lines:
    for _ in range(int(line[2:])):
        if   line[0] == "R": rope[0][0] += 1
        elif line[0] == "L": rope[0][0] -= 1
        elif line[0] == "U": rope[0][1] += 1
        elif line[0] == "D": rope[0][1] -= 1

        for i in range(1, len(rope)):
            hx, hy = rope[i-1]
            tx, ty = rope[i]
            
            if abs(hx - tx) <= 1 and abs(hy - ty) <= 1: continue
            elif hx > tx and hy > ty: tx += 1; ty += 1
            elif hx > tx and hy < ty: tx += 1; ty -= 1
            elif hx < tx and hy > ty: tx -= 1; ty += 1
            elif hx < tx and hy < ty: tx -= 1; ty -= 1
            elif hx > tx: tx += 1
            elif hx < tx: tx -= 1
            elif hy > ty: ty += 1
            elif hy < ty: ty -= 1

            rope[i] = [tx, ty]

        visited.add(tuple(rope[-1]))

print(len(visited))
