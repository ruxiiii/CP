# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        smallans1 = self.maxDepth(root.left)
        smallans2 = self.maxDepth(root.right)

        return max(smallans1,smallans2) + 1
