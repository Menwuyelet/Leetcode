from collections import defaultdict
nums = [3, 2, 1, 0]
# maximum = max(nums)
# minimum = min(nums)
# idx = [0] * (maximum-minimum+1)
# for num in nums:
#     idx[num - minimum] += 1

# index = 0
# for i, v in enumerate(idx):
#     for j in range(v):
#         nums[index] = i + minimum
#         index += 1

# print(nums)

# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
    
#     mid = len(nums)//2
#     left_half = merge_sort(nums[:mid])
#     right_half = merge_sort(nums[mid:])

#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

    
#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result


# sortedarr = merge_sort(nums)
# print(sortedarr)


def merge_sort(arr):
    if len(arr) <= 1:
         return arr
    
    mid = len(arr)//2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    ans = merge(left_half, right_half)
    return ans

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


ans = merge_sort(nums)
print(ans)