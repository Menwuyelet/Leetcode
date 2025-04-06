from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
ans = defaultdict(list)

## First Solution
# for s in strs:
#     count = [0] * 26
#     for c in s:
#         count[ord(c) - ord("a")] += 1
#     ans[tuple(count)].append(s)
# print(list(ans.values()))

## Second Solution
for s in strs:
    sortedS = sorted(s)
    ans["".join(sortedS)].append(s)

print(list(ans.values()))