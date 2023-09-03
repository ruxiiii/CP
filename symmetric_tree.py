# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        return self.isSameTree(root.left,root.right)

        # smallans1 = self.isSymmetric(root.left)
        # smallans2 = self.isSymmetrifc(root.right)

    def isSameTree(self,p: Optional[TreeNode], q: Optional[TreeNode]) :
        
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False


        smallans1 = self.isSameTree(p.left,q.right)
        smallans2 = self.isSameTree(p.right,q.left)

        if p.val == q.val and smallans1 and smallans2:
            return True

        return False
    

        
        
