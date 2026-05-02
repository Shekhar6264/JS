def solve(arr, operations):
    for start, end in operations:
        arr = arr[:start] + arr[start:end + 1][::-1] + arr[end + 1:]
    return arr
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
operations = [[0, 9], [4, 5], [3, 6], [2, 7], [1, 8], [0, 9]]
result = solve(arr, operations)
print("Result after operations: ", result)