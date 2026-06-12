def isPal(s):
    return s == s[::-1]

def solve(ind,s,path,ans):
    if ind == len(s):
        ans.append(path[:])
        return
    for i in range(ind,len(s)):
        if isPal(s[ind:i+1]):
            path.append(s[ind:i+1])
            solve(i+1,s,path,ans)
            path.pop()
ans=[]
solve(0,"aab",[],ans)
print(ans)