# Rucksack has 2 compartments of same len. Each char has a "priority": a-z = 1-26, A-Z = 27-52.
# For each rucksack, find chars that are in both its compartments. Sum their total priority

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

total = 0
for l in lines:
    dup = set(l[:len(l)//2]).intersection(set(l[len(l)//2:])).pop()
    total += ord(dup) - (96 if dup.islower() else 38)
    
print(total)
