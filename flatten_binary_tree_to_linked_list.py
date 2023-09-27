# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     #preorder m laana padega
    #     #with just modifying

        
    #     '''print(root.val)
    #     root.left
    #     root.right'''

    #     result = []
    #     result.append(root)
    #     result.append(None)

    #     while result:

    #         curNode = result.pop(0)

    #         if curNode:
    #             curNode.

    #             if curNode.left:
    #                 result.append(curNode.left)
    #             if curNode.right:
    #                 result.append(curNode.right)
            

    # def preorder(self, root):
    #     res = []
    #     def 
            
            




class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        result = []

        def preorder(root):
            if root:
                result.append(root)
                preorder(root.left)
                preorder(root.right)

        
        preorder(root)

        for i in range(1,len(result)):
            result[i-1].left = None
            result[i-1].right = result[i]



