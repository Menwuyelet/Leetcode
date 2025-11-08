n = 5 
left, right = 1, n
while left <= right:
    mid = left + (right - left) // 2
    if isBadVersion(mid) and not isBadVersion(mid-1):
        return mid
    elif isBadVersion(mid):
        right = mid - 1
    else:
        left = mid + 1