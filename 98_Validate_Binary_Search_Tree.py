# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, float("-inf"), float("inf"))
    def isValid(self, root, min, max):
        if not root: return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)


