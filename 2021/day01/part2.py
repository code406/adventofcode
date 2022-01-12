# Count the times the sum of measurements in a three-measurement 
# sliding window increases from the previous sum

with open("input.txt", "r") as input:
    nums = [int(i) for i in input.read().splitlines()]

count = 0
for i in range(len(nums)-3):
    window1 = nums[i], nums[i+1], nums[i+2]
    window2 = nums[i+1], nums[i+2], nums[i+3]
    if sum(window1) < sum(window2): count += 1
print(count)