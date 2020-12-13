# Infinite boot loop. Value of acc before 2nd iter starts?
with open("input.txt", "r") as input:
    lines = input.read().splitlines()

idx = 0
acc = 0
ran = []
while idx < len(lines) and idx not in ran:
    ran.append(idx)
    instr = lines[idx].split(" ")[0]
    value = int(lines[idx].split(" ")[1])

    if instr == "jmp": idx += value
    else:
        if instr == "acc": acc += value
        idx += 1

print(acc)
