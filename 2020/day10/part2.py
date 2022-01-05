# Joltage adapter chain. How many valid paths from outlet to device?
from functools import lru_cache

with open("input.txt", "r") as input:
    nums = [0] + sorted([int(i) for i in input.read().splitlines()])

@lru_cache(None)
def paths_to_device(i):
    if i == len(nums)-1: return 1 #WE GOT TO THE DEVICE!

    npaths = 0
    for nxt_i in range(i+1, len(nums)):
        if nums[nxt_i]-nums[i] > 3: break #No path from here
        npaths += paths_to_device(nxt_i)

    return npaths

print(paths_to_device(0))
