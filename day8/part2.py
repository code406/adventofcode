# Fix infinite loop by changing one nop or jmp. Whats acc?
with open("input.txt", "r") as input:
    og_lines = input.read().splitlines()

def test_run(fix_idx, wrong, right):
    lines = og_lines.copy()
    lines[fix_idx] = lines[fix_idx].replace(wrong, right)
    idx = 0
    acc = 0
    ran = []
    while idx not in ran:
        ran.append(idx)
        instr = lines[idx].split(" ")[0]
        value = int(lines[idx].split(" ")[1])

        if instr == "jmp": idx += value
        else:
            if instr == "acc": acc += value
            idx += 1
        if idx == len(lines): return acc
        continue

acc = 0
for fix_idx, line in enumerate(og_lines):
    instr = line.split(" ")[0]
    if instr == "nop": acc = test_run(fix_idx, "nop", "jmp")
    elif instr == "jmp": acc = test_run(fix_idx, "jmp", "nop")
    if acc: break

print(acc)
