def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l =merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])
    return merge(l, r)
def merge(l, r):
    sorted_arr =[]
    i = 0
    j = 0
    while i <len(l) and j <len(r):
        if l[i] < r[j]:
            sorted_arr.append(l[i])
            i += 1
        else:
            sorted_arr.append(r[j])
            j += 1
    while i < len(l):
        sorted_arr.append(l[i])
        i += 1
    while j < len(r):
        sorted_arr.append(r[j])
        j += 1
    return sorted_arr
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Merge sort: ", sorted_arr)