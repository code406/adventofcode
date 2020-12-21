# jf i hated this one
from math import ceil

with open("input.txt", "r") as input:
    buses = [int(i) for i in input.read().splitlines()[1].replace("x","1").split(",")]

time = 0
step = 1
for i, bus in enumerate(buses):
    while (time + i) % bus:
        time += step
    step *= bus

print(time)
