from collections import deque
def bipartite(graph):
    n = len(graph)
    for i in range(n):
        color = [-1] * n
        q = deque()
        q.append(i)
        color[i] = 0
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if color[nei] == -1:
                    color[nei] = 1 - color[node]
                    q.append(nei)
                elif color[nei] == color[node]:
                    return False
    return True
print(bipartite(graph = [[1,3],[0,2],[1,3],[0,2]]))
