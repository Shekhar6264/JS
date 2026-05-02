def longestsubstring(s):
    n = len(s)
    l = 0
    ans = 0
    v = set()
    for r in range(n):
        while s[r] in v:
            v.remove(s[l])
            l += 1
        v.add(s[r])
        ans = max(ans,r-l+1)
    return ans
s = "abcdbcabb"
result = longestsubstring(s)
print("Length of longest substring without repeating characters: ", result)