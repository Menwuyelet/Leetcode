people = [3,2,2,1]
limit = 3
people.sort()

left, right, count = 0, len(people)-1, 0

while left <= right:
    if people[right] == limit:
        count += 1
        right -= 1
    else:
        if people[left] + people[right] <= limit:
            count += 1
            left += 1
            right -= 1
        else:
            count += 1
            right -= 1
print(count)