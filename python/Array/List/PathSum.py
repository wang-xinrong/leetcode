# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, sum):
            if not root.left and not root.right:
                return sum+root.val==targetSum
            if not root.right:
                return helper(root.left, sum+root.val)
            if not root.left:
                return helper(root.right, sum+root.val)

            return helper(root.left, sum+root.val) or helper(root.right, sum+root.val)
        if not root:
            return False

        return helper(root, 0)

    def hasPathSumAlternative(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return target == root.val
        return self.hasPathSum( root.left, target - root.val) or \
               self.hasPathSum(root.right, target - root.val)