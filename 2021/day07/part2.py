# Make all numbers the same number but at the least cost
# Cost = sum(triangular number(differences between numbers and target))

with open("input.txt", "r") as input:
    l = list(map(int, input.read().split(",")))

print(min(sum(abs(i-l[j])*(abs(i-l[j])+1)//2 for j in range(len(l))) for i in range(max(l))))