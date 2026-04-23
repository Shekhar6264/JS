def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    l =[x for x in arr if x < pivot]
    m =[x for x in arr if x == pivot]
    r =[x for x in arr if x > pivot]
    return quicksort(l) + m + quicksort(r)
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Quick sort: ", sorted_arr)