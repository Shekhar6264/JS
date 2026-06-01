def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    l = [x for x in arr if x < pivot]
    m = [x for x in arr if x == pivot]
    r = [x for x in arr if x > pivot]
    return quick_sort(l)+m+quick_sort(r)
arr = [5,8,2,9,4]
print(quick_sort(arr))