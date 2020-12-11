# Find the 3 entries that sum to 2020 and multiply those 3 numbers together.
from itertools import combinations

with open("input.txt", "r") as input:
    nums = [int(i) for i in input.read().splitlines()]

for i,j,k in combinations(nums, 3):
    if i+j+k == 2020:
        print(i*j*k)
