strs = [""]
## First Solution
# sor_strs = sorted(strs, key=len)
# ans = sor_strs[0]
# found = False
# for i in range(len(ans)):
#     char = ans[i]
#     for j in strs:
#         if char != j[i]:
#             ans = ans[:i]
#             found = True
#     if found:
#         break

# print(ans)    

## Second Solution
ans = ""
for i in range(len(strs[0])):
    for j in strs:
        if i == len(j) or strs[0][i] != j[i]:
            print(ans)
            exit()
    ans += strs[0][i]
print(ans)
