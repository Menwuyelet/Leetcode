height =  [0,1,0,2,1,0,1,3,2,1,2,1]
## First solution
# lmax , rmax, minlr= [], [], []
# cmax = 0
# for i in height:
#     lmax.append(cmax)
#     if i > cmax:
#         cmax = i
# cmax = 0       
# for i in height[::-1]:
#     rmax.append(cmax)
#     if cmax < i:
#         cmax = i
# count = 0
# rmax.reverse()
# for i in range(len(height)):
#     minlr.append(min(lmax[i], rmax[i]))
#     if minlr[i] - height[i] >= 0:
#         count += minlr[i]-height[i]
#         # return cmax
# print(count)

## second solution

l= 0
r = len(height)-1
leftmax = height[l]
rightmax = height[r]

count = 0
while l < r:
    if leftmax < rightmax:
        l += 1
        leftmax = max(leftmax, height[l])
        count += leftmax - height[l]
    else:
        r -= 1
        rightmax = max(rightmax, height[r])
        count += rightmax - height[r]

print(count)