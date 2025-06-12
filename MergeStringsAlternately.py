word1, word2 = "abc", "pqr"
n = max(len(word1), len(word2))
merged = ""
w1, w2 = 0, 0
# for i in range(n+1):
#     if i % 2 == 0:
#         merged += word1[w1]
#         w1 += 1
#     else:
#         merged += word2[w2]
#         w2 += 1
# merged += word1[w1:]
# merged += word2[w2:]

for i in range(len(word1) + len(word2)):
    if w1 < len(word1) and i % 2 == 0:
        merged += word1[w1]
        w1 += 1
    elif w2 < len(word2) and i % 2 != 0:
        merged += word2[w2]
        w2 += 1

if w1 < len(word1):
    merged += word1[w1:]
if w2 < len(word2):
    merged += word2[w2:]


print(merged)