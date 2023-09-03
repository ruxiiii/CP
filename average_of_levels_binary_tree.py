# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #we use level order in this
        if root is None:
            return None

        queue=[]
        queue.append(root)
        res = []
    
     
        while queue:
            sum = 0
            level = len(queue)

            for i in range(len(queue)):
                curNode = queue.pop(0)
                sum += curNode.val
                
                if curNode.left:
                    queue.append(curNode.left)

                if curNode.right:
                    queue.append(curNode.right)

            res.append(round(sum/level, 5))
        
        return res
