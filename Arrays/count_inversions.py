def merge_sort(arr):
    if len(arr) <= 1:
        return arr,0
    if len(arr) > 1:
        mid = len(arr) // 2
        left , c1 = merge_sort(arr[:mid])
        right , c2 = merge_sort(arr[mid:])
        count = c1 + c2
        i = 0
        j = 0
        res = []
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                count += len(left) - i
                j += 1
        while i<len(left):
            res.append(left[i])
            i += 1
        while j<len(right):
            res.append(right[j])
            j += 1
        return res, count
print(merge_sort(arr=[3,5,4,2,1]))
