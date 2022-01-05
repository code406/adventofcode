# How much wait til the earliest bus, multiplied by its id
from math import ceil

with open("input.txt", "r") as input:
    buses = [int(i) for i in input.read().splitlines()[1].replace("x","0").split(",")]

for time in range(10000000000000000):
    flag = True
    for i, bus in enumerate(buses):
        if bus == 0: continue
        if bus*ceil(time/bus)-time != i:
            flag = False
            break
    if flag: break

print(time)
