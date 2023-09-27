# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(val = root_val)

        pos = inorder.index(root_val)

        root.left = self.buildTree(inorder[0:pos], postorder[:pos])
        root.right = self.buildTree(inorder[pos+1:], postorder[pos:])

        return root
        
        
