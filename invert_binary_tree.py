   # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None   

        smallans1 = self.invertTree(root.left)
        smallans2 = self.invertTree(root.right)

        root.left = smallans2
        root.right = smallans1


        return root


        
