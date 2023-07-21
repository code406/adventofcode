# the Elves are divided into groups of three, identified by their common char
# read input 3 by 3 lines, get priority of common char, add to total

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

total = 0
for i in range(0, len(lines), 3):
    dup = set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2])).pop()
    total += ord(dup) - (96 if dup.islower() else 38)
    
print(total)
