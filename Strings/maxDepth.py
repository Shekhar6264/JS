def maxDepth(s):
    o,c=0,0
    ans = 0
    for ch in s:
        if ch=='(':
            o+=1
        elif ch==')':
            c+=1
        ans = max(ans,o-c)
    return ans
s = "(1)+((2))+(((3)))"
print(maxDepth(s))
