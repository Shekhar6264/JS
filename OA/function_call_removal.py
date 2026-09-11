from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

# Remove function 0
removed = [False] * n
q = deque([0])
removed[0] = True

while q:
    node = q.popleft()

    for nei in graph[node]:
        if not removed[nei]:
            removed[nei] = True
            q.append(nei)

# Count functions that remain
answer = 0

for i in range(n):
    if not removed[i]:
        answer += 1

print(answer)