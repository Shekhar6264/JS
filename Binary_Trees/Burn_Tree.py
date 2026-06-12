from collections import deque
class Solution:
    def amountOfTime(self, root, start):
        parent = {}
        target = None
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == start:
                target = node
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)
        q = deque([target])
        vis = {target}
        time = 0
        while q:
            burned = False
            for _ in range(len(q)):
                node = q.popleft()
                if node.left and node.left not in vis:
                    vis.add(node.left)
                    q.append(node.left)
                    burned = True
                if node.right and node.right not in vis:
                    vis.add(node.right)
                    q.append(node.right)
                    burned = True
                if node in parent and parent[node] not in vis:
                    vis.add(parent[node])
                    q.append(parent[node])
                    burned = True
            if burned:
                time += 1
        return time