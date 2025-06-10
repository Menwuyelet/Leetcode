## first solution
from collections import defaultdict
nums = [3,0,1,0]
k = 1
count = defaultdict(int)
for i in nums:
    count[i] += 1
so_count = dict(sorted(count.items(), key=lambda item : item[1], reverse=True))
ans = []
for i, key in enumerate(so_count):
    if i >= k:
        break
    ans.append(key)
print(ans)