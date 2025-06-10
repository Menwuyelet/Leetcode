nums = [1,2,3,4]
n = len(nums)
answer = [1] * n

for i in range(1, n):
    answer[i] = answer[i - 1] * nums[i - 1]

suffix_product = 1
for i in reversed(range(n)):
    answer[i] *= suffix_product
    suffix_product *= nums[i]

print(answer)