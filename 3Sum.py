## first solution
nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
nums.sort()
vis = []
for  x, a in enumerate(nums):
    if x and a == nums[x-1]:
        continue
    target = 0 - a
    l = x+1
    r = len(nums)-1
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            vis.append([a, nums[l], nums[r]])
            l+=1
            while nums[l] == nums[l - 1] and l < r:
                l+=1

for i in vis:
    print(i)

