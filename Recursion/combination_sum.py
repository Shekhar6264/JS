def solve(ind, target, arr, ds, ans):
    if ind == len(arr):
        if target == 0:
            ans.append(ds[:])
        return
    if arr[ind] <= target:
        ds.append(arr[ind])
        solve(ind, target-arr[ind], arr, ds, ans)
        ds.pop()
    solve(ind+1, target, arr, ds, ans)
ans=[]
solve(0,7,[2,3,6,7],[],ans)
print(ans)