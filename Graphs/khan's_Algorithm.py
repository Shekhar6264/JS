from collections import deque
class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        indegree = [0] * V
        for node in range(V):
            for nei in adj[node]:
                indegree[nei] += 1
        q = deque()
        ans = []
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return ans

            