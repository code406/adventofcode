# Bingo. Multiply the sum of all unmarked numbers on the
# last winning board by the number that was just called

with open("input.txt", "r") as input:
    lines = input.read().splitlines()

nums = lines.pop(0).split(",")
lines = [x for line in lines for x in line.split(" ") if x != ""]
boards = list(zip(*[iter(zip(*[iter(lines)]*5))]*5))
marked = [[[0 for _ in range(5)] for _ in range(5)] for _ in boards]
winners = []

# Check boards for bingo
for n, num in enumerate(nums):
    for idx, board in enumerate(boards):
        if idx not in winners:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == num:
                        marked[idx][i][j] = True
                        if all(marked[idx][i]) or all(x[j] for x in marked[idx]):
                            winners.append(idx)
                            if len(winners) == len(boards):
                                print(int(num) * sum([int(x) for t in board for x in t if x not in nums[:n+1]]))