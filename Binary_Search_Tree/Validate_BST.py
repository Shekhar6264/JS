class Solution:
    def isValidBST(self, root):
        return self.valid(root,float('-inf'),float('inf'))
    def valid(self, root, mini, maxi):
        if not root:
            return True
        if root.val <= mini or root.val >= maxi:
            return False
        return (self.valid(root.left, mini, root.val) and self.valid(root.right, root.val, maxi))