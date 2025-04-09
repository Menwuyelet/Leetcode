nums = [2,0,2,1,1,0]
indx = [0]*(2+1)

for num in nums:
    indx[num] += 1

index = 0
for i, v in enumerate(indx):
    for j in range(v):
        nums[index] = i
        index += 1
