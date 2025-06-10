nums = [4,4,4,4,4,4]
k = 4

sum = [0]
current = 0
for i in nums:
    sum.append(current+i)
    current += i

seek = 1
count = 0
while seek < len(sum):
    if sum[seek] - sum[0] == k:
        count += 1
    hold = 1
    while hold < seek:
        if sum[seek] - sum[hold] == k:
            count += 1
        hold += 1
    seek += 1
print(count)