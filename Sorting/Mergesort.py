def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])
    return merge(l,r)
def merge(l,r):
    result = []
    i = 0
    j = 0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    while i < len(l):
        result.append(l[i])
        i += 1
    while j < len(r):
        result.append(r[j])
        j += 1
    return result
arr = [7,4,5,2,9]
print(merge_sort(arr))