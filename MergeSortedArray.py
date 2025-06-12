nums1 = [10,20,20,40,0,0]
m = 4
nums2 = [1,2]
n = 2

## first solution
x = m + n - 1
n1 = m-1
n2 = n-1
while n1 >= 0 and n2 >= 0:
    if nums1[n1] > nums2[n2]:
        nums1[x] = nums1[n1]
        n1 -= 1
    else:
        nums1[x] = nums2[n2]
        n2 -= 1
    x -= 1
while n2 >= 0:
    nums1[x] = nums2[n2]
    n2 -=1
    x -=1
print(nums1)