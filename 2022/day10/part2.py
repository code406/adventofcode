# "addX V": 2 cycles and adds V to X. noop: 1 cycle. X is the position of the
# middle of the sprite in a CRT of 40 dots per row. Sprite is '###'

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

# add an empty cycle for every addx
lines = [e for l in lines for e in (["", l] if l.startswith("addx") else [l])]

x = 1
crt = []
crt_line = ''
for cycle, line in enumerate(lines, 1):
    crt_line += "#" if (cycle % 40 - 1) in range(x-1, x+2) else "."
    if line.startswith("addx"): x += int(line[5:])
    if cycle % 40 == 0: crt.append(crt_line); crt_line = ''

print("\n".join(crt))
