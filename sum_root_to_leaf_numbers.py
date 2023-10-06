# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def sumfunc(root):
#         if not root:
#                 return 0

#         current_sum = current_sum * 10 + root.val

#         if not root.left and not root.right:
#                 return currentSum

#         return max(sumfunc(root.left), sumfunc(root.right))
        #have the access to every path
        #top to bottom
        #depth first
        #level order to depth first

        # sum = 0
        # maxSum = 0

        # res = []
        # res.append(root)
        # value = []
        # value.append(root.val)

        # while res:
        #     curNode = res.pop(0)
        #     if curNode.left:
        #         sum += value.pop
        

        # def sumfunc(root):
            
        #     maxSum = 0
        #     res = []
        #     sum = 0
        #     res.append(root)

        #     while res:
        #         curNode = res.pop(0)
        #         if root.left:
        #             sum += root.val
        #             sumfunc(root.left)

        #         if root.right:
    
        # y = sumfunc(root)
        # return y

class Solution:
    def helper(self, root, path):
        if root is None:
            return 0
        path += (str(root.val))

        if root.left is None and root.right is None:
            return int(path)

        leftSum = self.helper(root.left, path)
        rightSum = self.helper(root.right, path)
 
        return (int(leftSum) + int(rightSum))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, '')
