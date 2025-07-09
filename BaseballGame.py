ops = ["1","2","+","C","5","D"]
res = []

for _ in ops:
    if _ == "+" and len(res) >= 2:
        res.append(res[len(res)-1] + res[len(res)-2])
    elif _ == "C":
        res.pop()
    elif _ == "D" and len(res) >= 1:
        res.append(res[len(res)-1]*2)
    else:
        res.append(int(_))

print(sum(res))
    