# Definition for a binary tree node.
# Solution1 recursive
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res
    def inorder(self, root: TreeNode, res: List[int]) -> None:
        if not root: return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
# Solution2 stack
class Solution2:
    def inorderTraversal(self, root:TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
# 自己畫圖或是
# 參考 https://youtu.be/COBCEDPncus 可以得到很好的解釋。