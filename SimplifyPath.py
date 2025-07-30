path="/..//_home/a/b/..///"



stack = []
rev = ""
for _ in path + "/":
    if _ == "/":
        if rev == "..":
            if stack:
                stack.pop()
        elif rev != "." and rev != "":
            stack.append(rev)
        rev = ""
    else:
        rev += _
ans = "/"+"/".join(stack)
print(ans)