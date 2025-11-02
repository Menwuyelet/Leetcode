nums = [1, 0, 2, 3, 0, 11, 0, 5]
pr = 0

for se in range(1,len(nums)):
    if nums[pr] == 0 and nums[se]:
        nums[pr], nums[se] = nums[se], nums[pr]
        pr +=1
    elif nums[pr] != 0:
        pr +=1
print(nums)