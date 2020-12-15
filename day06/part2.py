# Add up the number of questions to which EVERYONE answered "yes" in each group
with open("input.txt", "r") as input:
    groups = input.read().rstrip().split("\n\n")

sum = 0
for group in groups:
    answers = [a for person in group.split("\n") for a in person]
    n_pers = len(group.split("\n"))
    counts = {i:answers.count(i) for i in answers}
    for count in counts.values():
        if count == n_pers:
            sum+=1

print(sum)
