from collections import deque
class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)
        visited = [0] * n
        def bfs(start,adj,visited):
            q = deque([start])
            visited[0] = 1
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if visited[nei] == 0:
                        visited[nei] = 1
                        q.append(nei)
        count = 0
        for i in range(n):
            if visited[i] == 0:
                bfs(i,adj,visited)
                count += 1
        return count
        
        
       