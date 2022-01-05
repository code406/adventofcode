# Joltage adapter chain. Number of 1-jolt-diffs * number of 3-jolt-diffs

with open("input.txt", "r") as input:
    nums = [0] + sorted([int(i) for i in input.read().splitlines()])

count_dicc = {"0": 0, "1": 0, "2": 0, "3": 1}
for i in range(len(nums)-1):
    diff = nums[i+1] - nums[i]
    if diff > 3: quit("There is no path to the device.")
    count_dicc[str(diff)] += 1

print(count_dicc["1"] * count_dicc["3"])
