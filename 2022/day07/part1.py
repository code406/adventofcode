from collections import defaultdict

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

sizes = defaultdict(int)
stack = []

for l in lines:
    if l.startswith("$ ls") or l.startswith("dir"):
        continue
    if l.startswith("$ cd"):
        dest = l.split()[2]
        if dest == "..":
            stack.pop()
        else:
            path = f"{stack[-1]}/{dest}" if stack else dest
            stack.append(path.replace("//", "/"))
    else:
        for path in stack:
            sizes[path] += int(l.split()[0])

# sum sizes of dirs with size <= 100000
print(sum([sizes[k] for k in sizes if sizes[k] <= 100000]))
