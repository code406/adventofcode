# "addX V": 2 cycles and adds V to X. noop: 1 cycle. strength = cycle*X
# get strength during 20th cycle and then every 40 cycles. get sum of strengths

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

# add an empty cycle for every addx
lines = [e for l in lines for e in (["", l] if l.startswith("addx") else [l])]

x = 1
strength = 0
for cycle, line in enumerate(lines, 1):
    if cycle % 40 == 20: strength += cycle * x
    if line.startswith("addx"): x += int(line[5:])

print(strength)
