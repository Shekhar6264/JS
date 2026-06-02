from collections import defaultdict
def checkValid(matrix):
    rows = defaultdict(set)
    cols = defaultdict(set)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            num = matrix[i][j]
            if num in rows[i] or num in cols[j]:
                return False
            rows[i].add(num)
            cols[j].add(num)
    return True
print(checkValid(matrix = [[1,2,3],[3,1,2],[2,3,1]]))