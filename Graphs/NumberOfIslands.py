from collections import deque
class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        def bfs(r,c):
            q = deque([(r,c)])
            grid[r][c] = '0'
            directions = [(0,-1),(-1,0),(1,0),(0,1)]
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if(0<=nr<rows and 0<=nc<cols and grid[nr][nc] == '1'):
                        grid[nr][nc] = '0'
                        q.append((nr,nc))
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfs(i,j)
                    islands += 1
        return islands