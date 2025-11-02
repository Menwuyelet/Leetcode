s =   "A man, a plan, a canal: Panama"

## first solution 
# filtered = "".join(char.lower() for char in s if char.isalnum())
# print(filtered == filtered[::-1])


## second solution
# filtered = "".join(char.lower() for char in s if char.isalnum())
# left, right = 0, len(filtered)-1
# while left < right:
#     if filtered[left] != filtered[right]:
#         print (False)
#         exit()
#     left += 1
#     right -= 1
# print (True)

## third solution 
# left, right = 0, len(s)-1

# while left < right:
#     while not(s[left].isalnum()):
#         left += 1
#     while not(s[right].isalnum()):
#         right -= 1
    
#     if s[left].lower() != s[right].lower():
#         print(False)
#         exit()
#     left, right = left + 1, right - 1
# print(True)

## Fourth solution
left, right = 0, len(s)-1

while left < right:
    if (s[left].isalnum() and s[right].isalnum()) and s[left].lower() != s[right].lower():
       x = s[left]
       y = s[right]
       print(False)
       exit()
    elif not(s[left].isalnum()):
        left +=1
    elif not(s[right].isalnum()):
        right -= 1
    else:
        left, right = left + 1, right - 1

print(True)
