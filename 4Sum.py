nums = [1, 0, -1, 0, -2, 2]
target = 0

nums.sort()
res, quad = [], []

def ksum(k, start, target):
    if k != 2:
        for i in range(start, len(nums) - k + 1):
            if i > start and  nums[i] == nums[i-1]:
                continue
            quad.append(nums[i])
            ksum(k-1, i+1, target-nums[i])
            quad.pop()
        return
    


    left, right = start, len(nums)-1
    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            res.append(quad + [nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1

ksum(4, 0, target)
print(res)