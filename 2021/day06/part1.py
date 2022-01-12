# Each day, 0 becomes 6 and adds a new 8. Every other number, -= 1
# How many lanternfish would there be after 80 days?

with open("input.txt", "r") as input:
    l = list(map(int, input.read().split(",")))

for _ in range(80):
    l = [6 if f == 0 else f-1 for f in l] + l.count(0)*[8]
print(len(l))