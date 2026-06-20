from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        q.append((0,0,1))
        grid[0][0] = 1
        while q:
            row, col, dist = q.popleft()
            if row == rows - 1 and col == cols - 1:
                return dist 
            directions = [(0,1),(1,0),(-1,0),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)]
            for dr,dc in directions:
                nr = dr + row
                nc = dc + col
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==0):
                    grid[nr][nc] = 1
                    q.append((nr,nc,dist+1))
        return -1