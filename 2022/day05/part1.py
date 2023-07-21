# Simulate stack movements and print the top of each stack

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

i = lines.index('')
figure, instructions = lines[:i-1], lines[i+1:]

figure = list(zip(*figure))[1::4]
figure = [list(reversed(''.join(x).strip())) for x in figure]

for i in instructions:
    s = i.split()
    amount, src, dst = int(s[1]), int(s[3]), int(s[5])
    figure[dst-1].extend([figure[src-1].pop() for _ in range(amount)])

print(''.join([x[-1] for x in figure]))
