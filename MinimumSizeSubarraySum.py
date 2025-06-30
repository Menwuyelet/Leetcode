target = 15
nums = [5,1,3,5,10,7,4,9,2,8]
# left = 0
# right = len(nums)-1

# total = sum(nums)
# if total < target:
#     print(0)
#     exit()
# while left < right:
#     if total - min(nums[right], nums[left]) >= target :
#         if min(nums[left], nums[right]) == nums[left]:
#             total -= nums[left]
#             left += 1
#         else:
#             total -= nums[right]
#             right -= 1
            
#     else:
#         break
# print (right)
# print(left)
# print(right - left + 1)


totalSum = sum(nums)
if totalSum < target:
    print(0)
    exit()
left = right = 0
total = 0
ans = float('inf')
for right in range(len(nums)):
    total += nums[right]
    while total >= target:
        ans = min(ans, right - left +1)
        total -= nums[left]
        left += 1
    
print(ans)