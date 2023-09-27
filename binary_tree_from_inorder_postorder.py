# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(val = root_val)

        pos = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:pos+1],inorder[0:pos]) 
        root.right = self.buildTree(preorder[pos+1:],inorder[pos + 1:])
        

        return root
