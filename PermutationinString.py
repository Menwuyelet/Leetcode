s1 = "ab"
s2 = "lecabee"

ls = list(s1)
ls2 = list(s2)
l = 0
r = len(s1) - 1
ans = False
while r < len(s2):
    a = sorted(ls)
    c = sorted(ls2[l:r+1])
    if c == a:
        ans = True
        break
    else:
        l += 1
        r += 1


print(ans)