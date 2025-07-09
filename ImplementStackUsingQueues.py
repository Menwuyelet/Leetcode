# class MyStack:

#     def __init__(self):
#           self.stack = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         if self.stack:
#             return self.stack.pop()
#         else:
#             return f"Stack is empty."
#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1]
#         else:
#             return f"Stack is empty."
#     def empty(self) -> bool:
#         if self.stack:
#             return False
#         else:
#             return True

from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

x = 10
y =11     
obj = MyStack()
obj.push(x)
obj.push(y)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)