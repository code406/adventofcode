# Find the 2 entries that sum to 2020 and multiply those 2 numbers together.
from itertools import combinations

with open("input.txt", "r") as input:
    nums = [int(i) for i in input.read().splitlines()]

for i,j in combinations(nums, 2):
    if i+j == 2020:
        print(i*j)
