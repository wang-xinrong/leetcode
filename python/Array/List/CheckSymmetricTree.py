# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def invertTree(self, root: Optional[TreeNode]):
        if not root:
            return root
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.invertTree(root.right)
        return self.isSameTree(root.left, root.right)

    def isSymmetricFaster(self, root: Optional[TreeNode]) -> bool:

        def check_mirror_image(root1, root2):

            if root1 == None and root2 == None:
                return True

            if root1 != None and root2 == None or root1 == None and root2 != None:
                return False

            if root1.val == root2.val:
                return check_mirror_image(root1.left, root2.right) and check_mirror_image(root1.right, root2.left)

        return check_mirror_image(root, root)
        