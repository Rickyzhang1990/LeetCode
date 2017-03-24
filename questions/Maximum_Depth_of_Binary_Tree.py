class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            depth = 0
        else:
            leftdepth = Solution.maxDepth(self, root.left)
            rightdepth = Solution.maxDepth(self, root.right)
            depth = max(leftdepth, rightdepth) + 1
        return depth 
