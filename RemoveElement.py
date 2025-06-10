nums = [4,4,0,1,0,2]
val = 0
## First Solution
# count = nums.count(val)
# nums.sort(key=lambda x:x==val)

# print(len(nums)- count)


## Second solution
i = -1
count = len(nums)
while i < len(nums)-1:
    if nums[i+1] != val:
        i += 1
    else:
        nums.remove(nums[i+1])
        nums.append(-1)
        count -= 1

print(count) 
