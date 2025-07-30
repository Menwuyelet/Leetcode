from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] += 1
    def pop(self) -> int:
        maxCount = max(self.freq.values())
        i = len(self.stack)-1
        while self.freq[self.stack[i]] != maxCount:
            i -= 1
        self.freq[self.stack[i]] -= 1
        return self.stack.pop(i)
freqStack = FreqStack()
freqStack.push(5); #// The stack is [5]
freqStack.push(7); #// The stack is [5,7]
freqStack.push(5); #// The stack is [5,7,5]
freqStack.push(7); #// The stack is [5,7,5,7]
freqStack.push(4); #// The stack is [5,7,5,7,4]
freqStack.push(5); #// The stack is [5,7,5,7,4,5]
freqStack.pop(); #// return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop(); #// return 7, as 5 and 7 is the