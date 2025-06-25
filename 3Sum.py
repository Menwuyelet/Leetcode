## first solution
nums = [-1,0,1,2,-1,-4]
# nums.sort()
# vis = []
# for  x, a in enumerate(nums):
#     if x and a == nums[x-1]:
#         continue
#     target = 0 - a
#     l = x+1
#     r = len(nums)-1
#     while l < r:
#         if nums[l] + nums[r] > target:
#             r -= 1
#         elif nums[l] + nums[r] < target:
#             l += 1
#         else:
#             vis.append([a, nums[l], nums[r]])
#             l+=1
#             while nums[l] == nums[l - 1] and l < r:
#                 l+=1

# for i in vis:
#     print(i)

## second solution

nums.sort()

def twosum(indx):
    target = 0 - nums[indx]
    left, right = indx+1, len(nums)-1
    temp = []
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left +=1
        else:
            temp.append([nums[indx], nums[left], nums[right]])
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -=1
            left += 1
            right -= 1
    return temp

ans = []
for i, a in enumerate(nums):
    if i and a == nums[i-1]:
        continue
    sum = twosum(i)
    ans.extend(sum)
print(ans)


