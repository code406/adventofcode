# Score of completing valid lines. Score starts at 0 and, for each 
# completed ), ], } or >, score *= 5 += 1,2,3 or 4 respectively.

def line_score(line):
    syms = {")": "(", "]": "[", "}": "{", ">": "<"}
    scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    stack = []
    for sym in line:
        if sym in "([{<": stack.append(sym)
        elif sym in ")]}>" and (not stack or stack.pop() != syms[sym]):
            return 0
    score = 0
    for sym in reversed(stack): score = score * 5 + scores[sym]
    return score

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

scores = sorted([s for s in [line_score(line) for line in lines] if s])
print(scores[len(scores)//2])