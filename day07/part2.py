# How many individual bags are required inside your single shiny gold bag?
with open("input.txt", "r") as input:
    lines = input.read().replace(".","").replace(" bags","").replace(" bag","").splitlines()

rules = {}
for line in lines:
    split1 = line.split(" contain ")
    if split1[1] == "no other":
        rules[split1[0]] = []
    else:
        split2 = split1[1].split(", ")
        rules[split1[0]] = [i.split(" ", 1) for i in split2]

def rec_sum(color):
    if not rules[color]: return 0
    return sum([int(r[0]) + int(r[0])*rec_sum(r[1]) for r in rules[color]])

print(rec_sum("shiny gold"))
