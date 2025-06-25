nums = [1,2,3,1,2,3]
k = 2

## first solution
visited = set()
start = 0
for end in range(len(nums)):
    if end - start > k:
        visited.remove(nums[start])
        start += 1
    if nums[end] in visited:
        print(True)
        exit()
    visited.add(nums[end])
print(False)

