nums = [2,4,5,6]
target = 9
idx = {}
for i, num in enumerate(nums):
    idx[num] = i

for i, num in enumerate(nums):
    difference = target - num
    if difference in idx and idx[difference] != i:
        print([i, idx[difference]])   
        break

# for i, n in enumerate(nums):
#     diffrence = target - n
#     if diffrence in idx:
#         print([idx[diffrence], i])
#     idx[n] = i