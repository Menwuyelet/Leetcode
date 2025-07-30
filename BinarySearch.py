nums = [-1,0,3,5,9,12]
target = 13



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
print(-1)

