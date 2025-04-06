## First Solution
# from collections import defaultdict
# nums = [6,5,5]
# count = defaultdict(int)
# ans = 0
# for i in nums:
#     count[i] += 1 
#     ans = ans if count[ans] > count[i] else i

# print(ans)

count, candidate = 0, 0
nums = [1,1,2,2,1,2,2,1,2]
for i in range(len(nums)):
    if count == 0:
        candidate = nums[i]
        count +=1
    else:
        count -=1
print(candidate)

