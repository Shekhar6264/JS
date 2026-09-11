from collections import deque

circles = []

n = int(input())

for _ in range(n):
    x, y, r = map(int, input().split())
    circles.append((x, y, r))


# Build graph
graph = [[] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):

        x1, y1, r1 = circles[i]
        x2, y2, r2 = circles[j]

        distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
        radius_sum_squared = (r1 + r2) ** 2

        if distance_squared <= radius_sum_squared:
            graph[i].append(j)
            graph[j].append(i)


# BFS
visited = [False] * n

def bfs(start):
    q = deque([start])
    visited[start] = True
    count = 0

    while q:
        node = q.popleft()
        count += 1

        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)

    return count


# Find largest connected component
maxgroup = 0

for i in range(n):
    if not visited[i]:
        group_size = bfs(i)
        maxgroup = max(maxgroup, group_size)

print(maxgroup)