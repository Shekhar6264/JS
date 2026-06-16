def dfs(node,adj,vis,st):
    vis[node] = 1
    for nei in adj[node]:
        if not vis[nei]:
            dfs(nei,adj,vis,st)
    st.append(node)
def topoSort(V,adj):
    vis = [0] * V
    st = []
    for i in range(V):
        if not vis[i]:
            dfs(i,adj,vis,st)
    ans = []
    while st:
        ans.append(st.pop())
    return ans