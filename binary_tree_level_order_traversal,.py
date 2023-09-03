# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return None
        
        queue = []
        queue.append(root)
        res = []

        while queue:
            level_values = []
            level_count = len(queue)

            for i in range(len(queue)):
                curNode = queue.pop(0)
                level_values.append(curNode.val)

                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)

            res.append(level_values)

        return res
