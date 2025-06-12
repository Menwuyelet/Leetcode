nums = [1,1,2,3,4]
## first solution
hold, seek = 0, 1
for i in range(len(nums)):
    n = len(nums)
    while seek < n and nums[hold] == nums[seek]:
        nums.pop(seek)
        n = len(nums)
    hold += 1
    seek += 1


