## First Solution
nums = [0,1,2,2,3,0,4,2]
val = 2
count = nums.count(val)
nums.sort(key=lambda x:x==val)

print(len(nums)- count)
