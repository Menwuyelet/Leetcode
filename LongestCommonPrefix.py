strs = ["flower","flow","flight"]
sor_strs = sorted(strs, key=len)
ans = sor_strs[0]
found = False
for i in range(len(ans)):
    char = ans[i]
    for j in strs:
        if char != j[i]:
            ans = ans[:i]
            found = True
    if found:
        break

print(ans)    

# res = ""
# found = False
# for i in range(len(strs[0])):
#     for j in strs:
#         if i == len(j) or j[i] != strs[0][i]:
#             res = res
#             found = True
#     if found:
#         break
#     res += strs[0][i]

# print(res)