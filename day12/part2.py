# Ships moving and turning WITH WAYPOINT
from collections import deque

def rotate(dicc, amount):
    values_deque = deque(dicc.values())
    values_deque.rotate(amount)
    return dict(zip(dicc.keys(), values_deque))

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

pos = {"N":0, "E":0,  "S":0, "W":0}
wpt = {"N":1, "E":10, "S":0, "W":0}

for line in lines:
    action = line[0]
    amount = int(line[1:])
    if   action=="R": wpt = rotate(wpt, int(amount/90))
    elif action=="L": wpt = rotate(wpt, -int(amount/90))
    elif action=="F": pos = {k: pos.get(k)+amount*wpt.get(k) for k in set(pos)}
    else: wpt[action] += amount

print(abs(pos["E"]-pos["W"]) + abs(pos["N"]-pos["S"]))
