# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l == 0 or r == 0:
            return l + r + 1
        else:
            return min(l, r) + 1

# Another kind of solution
class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.right or not root.left:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
                   # self.minDepth(root.left), self.minDepth(root.right) + 1 # one is zero
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
