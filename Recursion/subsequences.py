def subsequences(index,ans,arr,n,res):
    if index >= n:
        res.append(ans.copy())
        return
    ans.append(arr[index])
    subsequences(index+1,ans,arr,n,res)
    ans.pop()
    subsequences(index+1,ans,arr,n,res)
arr = [3,1,2]
index = 0
ans = []
res = []
n = len(arr)
subsequences(index,ans,arr,n,res)
print(res)