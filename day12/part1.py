# Ships moving and turning
with open("input.txt", "r") as input:
    lines = input.read().splitlines()

dirs = ["N","E","S","W"]
pos  = {dir:0 for dir in dirs}
face = 1 #E

for line in lines:
    action = line[0]
    amount = int(line[1:])
    if   action=="R": face = (face+int(amount/90))%len(dirs)
    elif action=="L": face = (face-int(amount/90))%len(dirs)
    else:
        if action=="F": action = dirs[face]
        pos[action] += amount

print(abs(pos["E"]-pos["W"]) + abs(pos["N"]-pos["S"]))
