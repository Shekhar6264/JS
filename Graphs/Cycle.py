from collections import deque
def cycle(i,adj,visited):
    q = deque()
    q.append((i,-1))
    visited[i] = 1
    while q:
        node,parent = q.popleft()
        for nei in adj[node]:
            if not visited[nei]:
                visited[nei] = 1
                q.append((nei,node))
            elif(nei!=parent):
                return True
    return False
adj = [[1],[0,2],[0,1]]
visited = [0] * len(adj)
print(cycle(0,adj,visited))
