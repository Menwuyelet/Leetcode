from collections import defaultdict
nums = [-10000, -10, -20, -1, -2,2 ,10,9,8,2,0,11,23,45,10,20]
maximum = max(nums)
minimum = min(nums)
idx = [0] * (maximum-minimum+1)
for num in nums:
    idx[num - minimum] += 1

index = 0
for i, v in enumerate(idx):
    for j in range(v):
        nums[index] = i + minimum
        index += 1

print(nums)

