# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?

with open("input.txt", "r") as input:
    elves = input.read().split("\n\n")
    
elves = [sum(map(int, e.split())) for e in elves]
print(sum(sorted(elves)[-3:]))