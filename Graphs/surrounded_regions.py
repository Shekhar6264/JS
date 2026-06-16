from collections import deque
class Solution:
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])
        vis = [[0] * cols for _ in range(rows)]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == rows-1 or r == 0 or c == 0 or c == cols-1):
                    q.append((r,c))
                    vis[r][c] = 1
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <=nr<rows and 0<=nc<cols and vis[nr][nc] == 0 and board[nr][nc] == 'O':
                    vis[nr][nc] = 1
                    q.append((nr,nc))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and vis[i][j] == 0:
                    vis[i][j] = 1
                    board[i][j] = 'X'

        