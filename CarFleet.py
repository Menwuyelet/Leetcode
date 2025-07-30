target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
stack = []
keypair = {}
for index, value in enumerate(position):
    keypair[value] = speed[index] 
position.sort(reverse=True)
for _ in position:
    tem = (target - _ )/ keypair[_]
    if stack and stack[-1] < tem:
        stack.append(tem)
    elif not stack:
        stack.append(tem)

print(len(stack))