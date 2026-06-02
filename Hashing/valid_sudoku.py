from collections import defaultdict
def isValidSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue
            box = ((r//3,c//3))
            if num in rows[r] or num in cols[c] or num in boxes[box]:
                return False
            rows[r].add(num)
            cols[c].add(num)
            boxes[box].add(num)
    return True
print(isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))