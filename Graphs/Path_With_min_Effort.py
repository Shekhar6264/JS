import heapq
class Solution:
    def minimumEffortPath(self, heights):
        n=len(heights)
        m=len(heights[0])
        q=[]
        heapq.heappush(q,(0,0,0))
        dist=[[float('inf')]*m for i in range(n)]
        dist[0][0]=0
        while q:
            effort,x,y=heapq.heappop(q)
            if x==n-1 and y==m-1:
                return effort
            for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
                X=x+dx
                Y=y+dy
                if 0<=X<n and 0<=Y<m :
                    new=max(effort,abs(heights[x][y]-heights[X][Y]))
                    if dist[X][Y]>new:
                        dist[X][Y]=new
                        heapq.heappush(q,(new,X,Y))
        return -1