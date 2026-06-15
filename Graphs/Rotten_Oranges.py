from collections import deque
class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid),len(grid[0])
        fo = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fo += 1
        if fo == 0:
            return 0
        mp = -1
        dire = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            mp += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dire:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fo -= 1
                        q.append((nr, nc))
        return mp if fo == 0 else -1