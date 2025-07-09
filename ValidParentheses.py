s = "()"
stack = []
dec = { ")" : "(" , "}" : "{", "]" : "[" }
for _ in s:
    if _ in ["(", "[", "{"]:
        stack.append(_)
    else:
        if stack:
            if stack[-1] == dec[_]:
                stack.pop()
            else:
                print(False)
                exit()
        else:
            print(False)
            exit()

if stack:
    print(False)
else:
    print(True)