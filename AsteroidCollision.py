asteroids =  [-2,-2,1,-2]
stack = []
stack.append(asteroids[0])
prev = 0
if stack[0] > 0:
    prev = 1
else:
    prev = -1

for i in range(1, len(asteroids)):
    if prev == 1:
        if (asteroids[i] > 0 ):
            stack.append(asteroids[i])
        else:
            re = True
            s = True
            while re and stack:
                if (abs(asteroids[i]) == abs(stack[-1])) and stack[-1] > 0:
                    stack.pop()
                    re = False
                    s = False
                elif (abs(asteroids[i]) > abs(stack[-1])) and stack[-1] > 0:
                    stack.pop()
                elif (abs(asteroids[i]) < abs(stack[-1])) and stack[-1] > 0:
                    re = False
                elif stack[-1] < 0:
                    stack.append(asteroids[i])
                    re = False
            if not stack and s:
                stack.append(asteroids[i])
                if prev == 1:
                    prev = -1
                else:
                    prev = 1
    else:
        stack.append(asteroids[i])
        if asteroids[i] > 0:
            prev = 1
        else: 
            prev = -1

print(stack)
