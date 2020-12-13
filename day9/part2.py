# Find a contiguous set of (>=2) nums which sum to the first invalid number
from itertools import combinations

with open("input.txt", "r") as input:
    nums = [int(i) for i in input.read().splitlines()]

preamble = 25
invalid_num = 0
for i, num in enumerate(nums[preamble:]):
    sums = [a+b for a,b in combinations(nums[i:i+preamble], 2)]
    if num not in sums:
        invalid_num = num
        break

def chunks(l, n):
    return [l[i:i+n] for i in range(len(l)) if len(l[i:i+n])==n]

for chunk_size in range(2, len(nums)):
    for chunk in chunks(nums, chunk_size):
        if sum(chunk) == invalid_num:
            print(min(chunk) + max(chunk))
            quit()
