s = "abc"
## first solution
# def palindrome(s, count = 0):
#     left, right = 0, len(s)-1
#     while left < right:
#         if s[left] != s[right]:
#             if count == 0:
#                 sls1 = s[:left] + s[left+1:]
#                 sls2 = s[:right] + s[right+1:]
#                 return palindrome(sls1, count+1) or palindrome(sls2, count+1)
#             else:
#                 return False
#         left, right = left + 1, right - 1
#     return True
# palindrome(s)

## second solution
left, right = 0 , len(s)-1
while left < right:
    if s[left] != s[right]:
        skipl = s[left + 1 : right + 1]
        skipr = s[left : right]
        print((skipl == skipl[::-1]) or (skipr == skipr[::-1]))
        exit()
    left += 1
    right -= 1

print(True)

## third solution
# def palindrome(left, right):
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# left, right = 0, len(s)-1
# while left < right:
#     if s[left] != s[right]:
#         print(((palindrome(left+1, right)) or (palindrome(left, right))))
#         exit()
# left += 1
# right -= 1
# print(True)