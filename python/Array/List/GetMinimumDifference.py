# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack=[]
        difference=float('inf')

        def pushallleft(root:Optional[TreeNode]):
            if not root:
                return
            while root:
                stack.append(root)
                root=root.left
        
        pushallleft(root)
        temp=stack.pop()
        prev=temp.val
        pushallleft(temp.right)
        while stack:
            temp=stack.pop()
            difference=min(difference, temp.val-prev)
            prev=temp.val
            pushallleft(temp.right)
        return difference
