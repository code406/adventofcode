# How many bag colors can eventually contain at least one shiny gold bag?
with open("input.txt", "r") as input:
    lines = input.read().replace(".","").replace(" bags","").replace(" bag","").splitlines()

rules = {}
for line in lines:
    split1 = line.split(" contain ")
    if split1[1] == "no other":
        rules[split1[0]] = []
    else:
        split2 = split1[1].split(", ")
        rules[split1[0]] = [i.split(" ", 1)[1] for i in split2]

def contains_gold(color, explored):
    if color in explored: return False
    if "shiny gold" in rules[color]: return True
    explored.append(color)
    return any([contains_gold(c, explored) for c in rules[color]])

print(sum([contains_gold(rule[0], []) for rule in rules.items()]))
