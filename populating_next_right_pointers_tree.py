class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = []
        queue.append(root)
        queue.append(None)  # Use None to separate levels
        while queue:
            curNode = queue.pop(0)

            if curNode:
                curNode.next = queue[0] if queue[0] is not None else None

                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)

            else:
                # Reached the end of a level, add None to separate levels
                if queue:
                    queue.append(None)

        return root
