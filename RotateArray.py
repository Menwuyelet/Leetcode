nums = [1,2,3,4,5,6,7]
k = 3
## First solution
# for i in range(k):
#     x = nums.pop()
#     nums.insert(0, x)

# print(nums)

## second solution
k = k % len(nums)

def reverse(left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1

reverse(0, len(nums) - 1)
reverse(0, k-1)
reverse(k, len(nums) - 1)
print(nums)