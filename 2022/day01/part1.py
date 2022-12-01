# Line: calories of an item of an elf. Blank lines separate elves.
# Total calories carried by the Elf carrying the most calories?

with open("input.txt", "r") as input:
    elves = input.read().split("\n\n")

elves = [sum(map(int, e.split())) for e in elves]
print(max(elves))