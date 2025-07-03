s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
if len(s) < len(t):
    print("")
    exit()


## first solution time limit exceed on test case 265
# ans = {}
# tl = list(t)
# l = 0

# for r in range(len(s)-len(t)+1):
#     tl = list(t)
#     if s[r] not in tl:
#         continue
#     l = r
#     for i in range(r, len(s)):
#         if s[i] in tl:
#             tl.remove(s[i])
#         elif i == (len(s)):
#             break
#         if len(tl) == 0:
#             ans[s[l:i+1]] = i-l
#             break

# if ans:
#     min_key = min(ans, key=ans.get)
#     print(min_key)
# else:
#     print("")

## second solution


wind, T = {}, {}
ans = [float('inf'), [0,0]]

for c in t:
    T[c] = 1 + T.get(c, 0)
have, need = 0 , len(T)
l = 0
for r in range(len(s)):
    if s[r] in t:
        wind[s[r]] = 1 + wind.get(s[r], 0)
        if wind[s[r]] == T[s[r]]:
            have += 1

    while have == need:
        if s[l] in t:
            wind[s[l]] -= 1
            if wind[s[l]] < T[s[l]]:
                have -= 1
        ans = min(ans, [r - l, [r,l]])
        l+=1
        
if ans[0] == float('inf'):
    print("")
else:
    print(s[ans[1][1] : ans[1][0]+1])
