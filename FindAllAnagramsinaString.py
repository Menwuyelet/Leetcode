from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        ps = Counter(p)
        k = len(p)
        window = Counter(s[:k])
        if window == ps:
            res.append(0)
        l,r = 0, k
        while r < len(s):
            window[s[r]] += 1
            window[s[l]] -= 1
            if window == ps:
                res.append(l+1)
            l +=1
            r+=1
        
        return res