# Horizontal position, depth and aim all start at 0
# Multiply final horizontal position by final depth

with open("input.txt", "r") as input:
    dirs = [i.split(" ") for i in input.read().splitlines()]

horiz, depth, aim = 0, 0, 0
for dir in dirs:
    if dir[0] == "up": aim -= int(dir[1])
    elif dir[0] == "down": aim += int(dir[1])
    elif dir[0] == "forward":
        horiz += int(dir[1])
        depth += int(dir[1]) * aim
print(horiz * depth)