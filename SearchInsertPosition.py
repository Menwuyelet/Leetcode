nums = [-1,0,2,4,6,8]
target = 10



left, right = 0, len(nums) - 1
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        print(mid) 
        exit() 
    elif nums[mid] < target:
        left = mid + 1  
    else:
        right = mid - 1  
print(left)