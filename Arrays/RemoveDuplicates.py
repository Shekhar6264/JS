def duplicates(arr):
    ind = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[ind]:
            ind += 1
            arr[ind] = arr[i]
    return ind + 1
arr = [1, 1, 2, 2, 3, 4, 4, 5]
result = duplicates(arr)    
print("Length of array after removing duplicates: ", result)