# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum=0
        def helper(root: Optional[TreeNode], carry: int):
            if not root.left and not root.right:
                self.sum+=10*carry+root.val
            if root.left:   
                helper(root.left, 10*carry+root.val)

            if root.right:
                helper(root.right, 10*carry+root.val)
        helper(root, 0)
        return self.sum

    def sumNumbersFaster(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, node: TreeNode, num: int) -> int:
        if not node:
            return 0
        if not node.left and not node.right:
            return num * 10 + node.val
        return self.dfs(node.left, num * 10 + node.val) + self.dfs(node.right, num * 10 + node.val)