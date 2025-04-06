s = "rat"
t = "car"

## First Solution
# freq = {}
# for i in s:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# for i in t:
#     if i in s:
#         freq[i] -=1
#     else:
#         freq[i] = 1

# ans = True
# for i in freq:
#     if freq[i] != 0:
#         ans = False
#         break
# print(ans)

## Second Solution
# s = "rat"
# t = "cat"

# lss = list(s)
# lss.sort()

# lst = list(t)
# lst.sort()
# if lss == lst:
#     print("true")
# else:
#     print("false")

## Third Solution
if len(s) != len(t):
    print("false")
else:
    countS = {}
    countT = {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

print(countT == countS)