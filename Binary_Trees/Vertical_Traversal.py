from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root):
        mp = defaultdict(list)
        q = deque([(root, 0, 0)])
        while q:
            node, row, col = q.popleft()
            mp[col].append((row, node.val))
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        ans = []
        for col in sorted(mp.keys()):
            nodes = sorted(mp[col])
            temp = []
            for row, val in nodes:
                temp.append(val)
            ans.append(temp)
        return ans