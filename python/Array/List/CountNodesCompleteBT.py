# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left=self.leftheight(root)
        right=self.rightheight(root)

        if left==right:
            return 2**left-1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        

    def leftheight(self, root: Optional[TreeNode]) -> int:
        height=0
        while root:
            height+=1
            root=root.left
        return height

    def rightheight(self, root: Optional[TreeNode]) -> int:
        height=0
        while root:
            height+=1
            root=root.right
        return height
