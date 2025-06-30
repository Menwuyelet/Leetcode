# from collections import defaultdict
arr = [2,3,4]
k = 3
x = 1

pair = []
for r in range(len(arr)):
    pair.append([r, abs(arr[r] - x)])

sortedPair = sorted(pair, key = lambda x: x[1])
ans = []
for i in range(k):
    if i > len(arr) - 1 and sortedPair[i][1] == sortedPair[i+1][1]:
        ans.append(arr[min(sortedPair[i][0], sortedPair[i+1][0])])
    else:
        ans.append(arr[sortedPair[i][0]])

print(sorted(ans))

