nums = [1,2]
## first solution
x = len(nums)//3
ans = []
visited = set()
for i in nums:
    if i not in visited and nums.count(i) > x:
        ans.append(i)
        visited.add(i)
print(ans)

## second solution
# from collections import defaultdict
# val = len(nums)//3
# visited = defaultdict(int)
# ans = []
# suf = set()
# for i in nums:
#     if i not in suf:
#         visited[i] += 1
#         if visited[i] > val:
#             ans.append(i)
#             suf.add(i)

# print(ans)