def characterReplacement(s,k):
    l = 0
    n =len(s)
    ans = 0
    mf = 0
    freq = {}
    for r in range(n):
        freq[s[r]] = freq.get(s[r],0) + 1
        mf = max(mf,freq[s[r]])
        while r-l+1 - mf > k:
            freq[s[l]] -= 1
            l += 1
        ans = max(ans,r-l+1)
    return ans
s = "ABABA"
k = 2
result = characterReplacement(s, k)
print("Length of longest substring after character replacement: ", result)