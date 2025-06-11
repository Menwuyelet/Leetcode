s = "abc"
## first solution
def palindrome(s, count = 0):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            if count == 0:
                sls1 = s[:left] + s[left+1:]
                sls2 = s[:right] + s[right+1:]
                return palindrome(sls1, count+1) or palindrome(sls2, count+1)
            else:
                return False
        left, right = left + 1, right - 1
    return True
palindrome(s)
