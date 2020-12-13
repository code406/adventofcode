# Find 1st which is not sum of two of the 25 numbers before it (excl. preamble)
from itertools import combinations

with open("input.txt", "r") as input:
    nums = [int(i) for i in input.read().splitlines()]

preamble = 25
for i, num in enumerate(nums[preamble:]):
    sums = [a+b for a,b in combinations(nums[i:i+preamble], 2)]
    if num not in sums:
        print(num)
        break
