s = "2[a3[b]]c"
stackCh = []
ans = ""
for i in range(len(s)):
    if s[i] != "]":
        stackCh.append(s[i])
    else:
        sub = ""
        while stackCh[-1] != "[":
            sub = stackCh.pop()+ sub
        stackCh.pop()
        num = ""
        while stackCh and stackCh[-1] in ["0","1","2","3","4","5","6","7","8","9"]:
            num = stackCh.pop() + num
        
        inum = int(num)
        temp = ""
        for i in range(inum):
            temp += sub
        stackCh.append(temp)

print("".join(stackCh))