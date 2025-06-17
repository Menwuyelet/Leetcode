nums = [1,1,2,3,4]
## first solution
# hold, seek = 0, 1
# for i in range(len(nums)):
#     n = len(nums)
#     while seek < n and nums[hold] == nums[seek]:
#         nums.pop(seek)
#         n = len(nums)
#     hold += 1
#     seek += 1

## second solution

# n = len(nums)
# l = r = 0

# while r < n:
#     nums[l] = nums[r]
#     while r < n and nums[l] == nums[r]:
#         r += 1
#     l += 1

# print(l)

## third solution

n = len(nums)
l = 1
for r in range(1, n):
    if nums[r] != nums[r-1]:
        nums[l] = nums[r]
        l += 1

print(l)
print(nums)

