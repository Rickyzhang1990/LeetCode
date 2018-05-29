# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.iss(root.left , root.right)
        
    def iss(self , left ,right):
        if left == None  and right == None:
            return True 
        elif left == None or right == None:
            return False
        if left.val != right.val:
            return False     
        return self.iss(left.left , right.right) and self.iss(left.right , right.left)
