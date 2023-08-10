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

# total disk is 70000000 and we need unused space of 30000000
need_to_free = 30000000 - (70000000 - sizes["/"])

# Find smallest dir that would free up that much space. Print its size
print(min([v for v in sizes.values() if v > need_to_free]))
