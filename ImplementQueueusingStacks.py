class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)


    def pop(self) -> int:
 
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        x = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return x
    def peek(self) -> int:
        lenn = len(self.stack1)-1
        while lenn + 1:
            self.stack2.append(self.stack1[lenn])
            lenn -= 1
        x = self.stack2[-1]
        self.stack2.clear()
        return x
    

    def empty(self) -> bool:
        if self.stack1:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:

x = 1
y = 2
obj = MyQueue()
obj.push(x)
obj.push(y)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_3)
print(param_2)

print(param_4)