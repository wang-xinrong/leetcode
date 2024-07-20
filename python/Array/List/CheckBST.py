# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float('-inf'), float('inf'))
        
    def check(self, root: Optional[TreeNode], a: int, b:int):
        if not root:
            return True
        c=root.val<b and root.val>a
        return c and self.check(root.left, a, root.val) and self.check(root.right, root.val, b)