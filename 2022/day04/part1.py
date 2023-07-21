# Assignments format: 2-8,3-7 (per line) Find if either fully contains the other.
# In how many lines does it happen? 

with open("input.txt", "r") as input:
    lines = input.read().splitlines()
    
total = 0
for l in lines:
    a = [x.split('-') for x in l.split(',')]
    range1 = set(range(int(a[0][0]), int(a[0][1])+1))
    range2 = set(range(int(a[1][0]), int(a[1][1])+1))
    if range1.issubset(range2) or range2.issubset(range1):
        total += 1

print(total)
