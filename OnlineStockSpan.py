class StockSpanner:

    def __init__(self):
        self.stack = []
        self.temp = []
        self.dec = {}

    def next(self, price: int) -> int:
        self.temp.append(price)
        count = 1
        x = len(self.stack)-1
        while self.stack and self.stack[x] <= price:
            self.temp.append(self.stack[x])
            count += self.dec[x]
            x -= self.dec[x]
            
            if x < 0:
                break
        
        # if self.temp:
        self.stack.append(self.temp[0])
        self.temp.clear()
        self.dec[len(self.stack)-1] = count
        return count
    
    

stockSpanner = StockSpanner()
print(stockSpanner.next(100))
print(stockSpanner.next(80))
print(stockSpanner.next(60))
print(stockSpanner.next(70))
print(stockSpanner.next(60))
print(stockSpanner.next(75))
print(stockSpanner.next(85))