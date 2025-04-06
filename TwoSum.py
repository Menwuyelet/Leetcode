nums = [3,2,4]
target = 6

## First Solution
# idx = {}
# for i, num in enumerate(nums):
#     idx[num] = i

# for i, num in enumerate(nums):
#     difference = target - num
#     if difference in idx and idx[difference] != i:
#         print([i, idx[difference]])   
#         break

## Second Solution
numsHash = {}
for i in range(len(nums)):
    num = target - nums[i]
    if num in numsHash:
        print(numsHash[num], i)
        break
    else:
        numsHash[nums[i]] = i

## Third Solution
# numsHash = {}
# for i in range(len(nums)):
#     numsHash[nums[i]] = i

# for i in range(len(nums)):
#     num = target - nums[i]
#     if num in numsHash and numsHash[num] != i:
#         print([i, numsHash[num]])
#         break
    