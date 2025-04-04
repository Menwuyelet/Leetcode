nums = [1,2,3,4]
numsset = set(nums)
ans = False
if len(numsset) < len(nums):
    ans = True
print(ans)