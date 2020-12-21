# How much wait til the earliest bus, multiplied by its id
from math import ceil

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

now = int(lines[0])
buses = [int(b) for b in lines[1].split(",") if b!="x"]

best_bus = 0
best_diff = 999999999
for bus in buses:
    diff = bus*ceil(now/bus) - now
    if diff < best_diff:
        best_diff = diff
        best_bus = bus

print(best_bus * best_diff)
