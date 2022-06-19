# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isSym(root.left, root.right)
    def isSym(self, l: TreeNode, r: TreeNode) -> bool:
        if not l and not r: return True
        if not l or not r: return False
        return l.val == r.val and self.isSym(l.left, r.right) and self.isSym(l.right, r.left)

# Solution 2 Queue
from collections import deque
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = deque([(root.left, root.right)])
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if node1 and node2 and node1.val == node2.val:
                queue.append((node1.left, node2.right))
                queue.append((node1.right, node2.left))
            else:
                return False
        return True

