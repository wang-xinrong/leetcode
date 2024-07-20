# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        def pushallleft(root: Optional[TreeNode]):
            if not root:
                return
            while root:
                stack.append(root)
                root=root.left
        pushallleft(root)
        while stack:
            temp=stack.pop()
            if k==1:
                return temp.val
            k-=1
            pushallleft(temp.right)

    def kthSmallestFaster(self, root: Optional[TreeNode], k: int) -> int:
        self.count=0
        self.res=0
        self.inorderTraversal(root, k)
        return self.res
        

    def inorderTraversal(self, root: Optional[TreeNode], k: int):
        if not root or self.count>=k:
            return
        left=self.inorderTraversal(root.left, k)
        self.count+=1
        if self.count == k:
            self.res=root.val
        self.inorderTraversal(root.right, k)