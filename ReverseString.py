s = ["H","a","n","n","a","h"]
## first solution
# left = 0
# right = len(s)-1
# while left < right:
#     s[left], s[right] = s[right], s[left]
#     left += 1
#     right -= 1
# print(s)

## second solution
# n = len(s)
# for i in range(n):
#     s.insert( n, s[i])

# s = s[n:]
# print(s)

## third solution 

stack = []
for char in s:
    stack.append(char)

i = 0
while stack:
    s[i] = stack.pop()
    i+=1

print(s)