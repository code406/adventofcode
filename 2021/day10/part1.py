# Chunks open with (, [, { or <, and close with ), ], } or >.
# score += 3, 57, 1197, 25137 if illegal close bracket respectively.

def line_score(line):
    syms = {")": "(", "]": "[", "}": "{", ">": "<"}
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    stack = []
    for sym in line:
        if sym in "([{<": stack.append(sym)
        elif sym in ")]}>" and (not stack or stack.pop() != syms[sym]):
            return scores[sym]
    return 0

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

print(sum(line_score(line) for line in lines))