s =  "Was it a car or a cat I saw?"

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

left, right = 0, len(s)-1

while left < right:
    while not(s[left].isalnum()):
        left += 1
    while not(s[right].isalnum()):
        right -= 1
    
    if s[left].lower() != s[right].lower():
        print(False)
        exit()
    left, right = left + 1, right - 1
print(True)