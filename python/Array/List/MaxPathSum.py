# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max=float('-inf')
        self.helper(root)
        return self.max

    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        left=self.helper(root.left)
        right=self.helper(root.right)
        left, right = left if left > 0 else 0, right if right > 0 else 0
        self.max=max(self.max, left+right+root.val)
        return root.val+max(left, right)
        # alternatively 
        # return max(root.val+max(left, right), 0)
        