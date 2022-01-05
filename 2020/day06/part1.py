# Add up the number of questions to which anyone answered "yes" in each group
with open("input.txt", "r") as input:
    groups = input.read().split("\n\n")

sum = 0
for group in groups:
    answers = {a for person in group.split("\n") for a in person}
    sum += len(answers)

print(sum)
