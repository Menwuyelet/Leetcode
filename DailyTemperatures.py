temperatures = [73,74,75,71,69,72,76,73]
res = [0]*len(temperatures)

stack = []
for i in range(len(temperatures)):
    if not stack:
        stack.append([temperatures[i], i])
    else:
        while stack[-1][0] < temperatures[i]:
            idx = stack[-1][1]
            stack.pop()
            res[idx] = i - idx
            if len(stack) == 0:
                break
        stack.append([temperatures[i], i])

print(res)


