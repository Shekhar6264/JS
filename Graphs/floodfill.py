from collections import deque
class Solution:
    def floodFill(self, grid, sr, sc, color):
        rows = len(grid)
        oldcolor = grid[sr][sc]
        cols = len(grid[0])
        if oldcolor == color:
            return grid
        def bfs(r,c):
            q = deque([(r,c)])
            grid[r][c] = color
            directions = [(0,-1),(-1,0),(1,0),(0,1)]
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if(0<=nr<rows and 0<=nc<cols and grid[nr][nc] == oldcolor):
                        grid[nr][nc] = color
                        q.append((nr,nc))
        bfs(sr,sc)
        return grid
        