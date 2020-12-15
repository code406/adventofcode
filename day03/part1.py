# Starting top-left, following right 3 and down 1, how many trees do you encounter?
slope = [3, 1]

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

maplen = len(lines[0])
x = 0
bumps = 0
for i, l in enumerate(lines):
    if i % slope[1]: continue
    if l[x]=="#": bumps += 1
    x = (x + slope[0]) % maplen

print(bumps)
