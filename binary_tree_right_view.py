# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return None


        #level order traversal
        queue = []
        pvalue = []
        queue.append(root)
        res = []

        while len(queue) !=0 :
            for i in range(len(queue)):
                curNode = queue.pop(0)
                pvalue.append(curNode.val)
                if curNode.left is not None:
                    queue.append(curNode.left)
                if curNode.right is not None:
                    queue.append(curNode.right)

            pvalue.append(' ')

        for j in range(len(pvalue)):
            if pvalue[j] == ' ':
                res.append(pvalue[j-1])


        return res


###way 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            #level order
        if root is None:
            return None

        queue = []
        queue.append(root)
        res = []

        while(len(queue)!= 0):
            n = len(queue)
            for i in range(n):
                curNode = queue.pop(0)
                if i == n-1:
                    res.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
        return res

            
