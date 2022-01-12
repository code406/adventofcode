# Count the times a depth measurement increases 
# from the previous measurement

with open("input.txt", "r") as input:
    nums = [int(i) for i in input.read().splitlines()]

count = 0
for i in range(len(nums)-1):
    if nums[i] < nums[i+1]: count += 1
print(count)