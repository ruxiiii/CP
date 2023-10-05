'''to find maximum number in a tree'''
#finding max
def findmax(root):
  if root is None:
    return None
  
  leftmax = findmax(root.left)
  rightmax = findmax(root.right)

  return max(leftmax,rightmax,root.val)


#wrong approach not traversing iteratively, not be solved using dynamix
def max(node):
  if node is None:
    return None
  
  res = []

  if node.left:
    res.append(node.left)

  if node.right:
    res.append(node.right)

  return max(res)




'''find sum of all values in tree'''
def sum(node):
  queue = []
  queue.append(node)
  res = []

  while queue:
    for i in range(len(queue)):
      curNode = queue.pop(0)

      if curNode.left:
        queue.append(curNode.left)
      if curNode.right:
        queue.append(curNode.right)
    
    res.append(curNode.val)
  
  return sum(res)


def sumtree(root):
  if root is None:
    return 0
  
  smallans1 = sumtree(root.left)
  smallans2 = sumtree(root.right)
  
  return smallans1 + root.val + smallans2




'''max of each level'''
def maxlevel(root):
  queue = []
  queue.append(root)
  res = []
  

  while queue:
    level_values = []
    for i in range(len(queue)):
      curNode = queue.pop(0)
      level_values.append(curNode.val)

      if curNode.left:
        queue.append(curNode.left)

      if curNode.right:
        queue.append(curNode.right)

    
    res.append(max(level_values))
  
  return res



#####using deque() makes the time complexity as 0(1) becuase when doing with normal queue, after pop(0), elements shifted to left

'''max of each level'''

from collections import deque
def maxlevel(root):
  queue = deque()
  queue.append(root)
  res = []
  

  while queue:
    level_values = []
    for i in range(len(queue)):
      curNode = queue.pop(0)
      level_values.append(curNode.val)

      if curNode.left:
        queue.append(curNode.left)

      if curNode.right:
        queue.append(curNode.right)

    
    res.append(max(level_values))
  
  return res






'''inorder, post and pre'''
def inorder(node):
  if node is None:
    return None
  
  inorder(node.left)
  print(node.val)
  inorder(node.right)

def pre(node):
  if node is None:
    return None
  
  print(node.val)
  pre(node.left)
  pre(node.right)

def post(node):
  if node is None:
    return None
  
  post(node.left)
  post(node.right)
  print(node.val)





'''Good job on completing it!'''
