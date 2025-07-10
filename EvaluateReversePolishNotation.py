tokens = ["1","2","+","3","*","4","-"]
stack = []
for _ in tokens:
    if _ not in ["+","-","/","*"]:
        stack.append(int(_))
    else:
        a = stack.pop()
        b = stack.pop()
        if _ == "+":
            stack.append(a+b)
        elif _ == "-":
            stack.append(b-a)
        elif _ == "*":
            stack.append(a*b)
        else:
            stack.append(int(b/a))

print(stack[0])