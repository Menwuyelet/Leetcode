from collections import defaultdict
s = "AAABABB"
k = 1
# ans = 0
# left = 0
# count = defaultdict(int)
# count[s[0]] = 1
# for right in range(len(s)-1):
#     max_val = max(count.values())
#     if (right - left + 1) - max_val <= k:
#         if s[right] == s[right+1]:
#             count[s[right]] += 1
#         else:
#             count[s[right+1]] += 1
#     else:
#         ans = max(ans, right - left)
#         count[s[left]] -= 1
#         left += 1
# ans = max(ans, right + 1 - left)

# ans = 0
# temp = 0
# count = defaultdict(int)
# left = 0
# count[s[0]] = 0
# for right in range(len(s)):
#     if (right - left + 1) - max(count.values()) <= k:
#         temp += 1
#         count[s[right]] += 1
#     else:
#         ans = max(ans, temp)
#         while temp - max(count.values()) > k:
#             count[s[left]] -= 1
#             left += 1
#             temp -= 1
# ans = max(ans, temp)


count = defaultdict(int)
maxf = 0
ans = 0
left = 0
for right in range(len(s)):
    count[s[right]] += 1
    maxf = max(maxf, count[s[right]])
    while (right - left + 1) - maxf > k:
        count[s[left]]-= 1
        left += 1
    ans = max(ans, right - left + 1)

print(ans)
