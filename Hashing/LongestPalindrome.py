from collections import Counter
def longestPalindrome(s):
    ans = 0
    d = Counter(s)
    odd_found = False
    for i in d.values():
        if i % 2 == 0:
            ans += i
        else:
            odd_found = True
            ans += i-1
    if odd_found:
        ans += 1
    return ans
print(longestPalindrome('abccccdd'))