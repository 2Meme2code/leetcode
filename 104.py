class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1) if root else 0
