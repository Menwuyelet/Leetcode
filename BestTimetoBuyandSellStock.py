prices = [2,1,2,1,0,1,2]
l = 0
r = 1
maxp = 0
while r < len(prices):
    if prices[l] < prices[r]:
        maxp = max(maxp, (prices[r] - prices[l]))
    else:
       l = r
    r+=1
print(maxp)
