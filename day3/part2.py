# Starting top-left, multiply the number of trees encountered in each of the slopes
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

maplen = len(lines[0])
total_bumps = 1
for slope in slopes:
    x = 0
    bumps = 0
    for i, l in enumerate(lines):
        if i % slope[1]: continue
        if l[x]=="#": bumps += 1
        x = (x + slope[0]) % maplen
    total_bumps *= bumps

print(total_bumps)
