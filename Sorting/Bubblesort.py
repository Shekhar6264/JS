arr = [3,1,5,7,2,4,6,8]
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Bubble sort: ",arr)