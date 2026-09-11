from collections import deque
grid = [
    list("11000"),
    list("11000"),
    list("00100"),
   list("00011")
]
k = 2
rows = len(grid)
cols = len(grid[0])
visited = set()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(r, c):
    q = deque([(r, c)])
    visited.add((r, c))
    boundary_sum = 0

    while q:
        row, col = q.popleft()
        is_boundary = False

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                is_boundary = True
            elif int(grid[nr][nc]) == 0:
                is_boundary = True
            elif (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))

        if is_boundary:
            boundary_sum += int(grid[row][col])

    return boundary_sum

qualified_islands = 0
for i in range(rows):
    for j in range(cols):
        if int(grid[i][j]) != 0 and (i, j) not in visited:
            boundary_sum = bfs(i, j)
            if boundary_sum % k == 0:
                qualified_islands += 1

print(qualified_islands)