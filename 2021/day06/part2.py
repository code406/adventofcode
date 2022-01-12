# Each day, 0 becomes 6 and adds a new 8. Every other number, -= 1
# How many lanternfish would there be after 256 days?

with open("input.txt", "r") as input:
    l = list(map(int, input.read().split(",")))

fishes_in_day = [0]*9
for f in l: fishes_in_day[f] += 1
for day in range(256):
    fishes_in_day[7] += fishes_in_day[0]
    fishes_in_day = fishes_in_day[1:] + [fishes_in_day[0]]
print(sum(fishes_in_day))