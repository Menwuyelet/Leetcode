height = [1,8,6,2,5,4,8,3,7]

left, right , highest = 0, len(height)-1, 0

while left < right:
    y = min(height[left], height[right])
    x = right - left
    highest = max(highest, y * x)
    if height[left] < height[right]:
        left +=1
    else:
        right -=1

print(highest)