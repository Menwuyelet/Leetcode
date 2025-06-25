s = ""

visited = set()
ans = 0
left = 0

for right in range(len(s)):
    if s[right] in visited:
        ans = max(ans, right - left)
        while s[right] in visited:
            visited.remove(s[left])
            left += 1
    visited.add(s[right])
ans = max(ans, len(s) - left)
print (ans)