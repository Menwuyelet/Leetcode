class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = float('inf')
        self.count = {}
        self.prevMin = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count[val] = 1 + self.count.get(val, 0)
        if val < self.minn:
            self.prevMin.append(self.minn)
            self.minn = val
    def pop(self) -> None:
        x = self.stack.pop()
        self.count[x] -= 1
        if x == self.minn and self.count[x] == 0:
            self.minn = self.prevMin.pop()
        elif x < self.minn and self.count[x] == 0:
            self.prevMin.remove(x)
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top() )  
print(minStack.getMin())