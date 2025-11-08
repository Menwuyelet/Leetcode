nums = [5,7,7,8,8,10]
target = 8
l, r = 0, len(nums) - 1
ans = []
while l <= r:
    mid = l + (r-l) // 2
    if nums[mid] == target:
        left = right = mid
        while left >= 0 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1
        ans = [left+1, right-1]
        break
    elif nums[mid] > target:
        r = mid - 1
    else:
        l = mid + 1
    
else:
    ans = [-1, -1]
    
print(ans)