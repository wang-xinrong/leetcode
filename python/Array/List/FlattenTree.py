# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     def formChain(root: Optional[TreeNode]) -> Optional[TreeNode]:
    #         if not root:
    #             return None
            
    #         if not root.left and not root.right:
    #             return root

    #         if not root.left:
    #             return formChain(root.right)
    #         else:
    #             tail=formChain(root.left)
    #             tail_2=formChain(root.right)
    #             tail.right=root.right
    #             tail.left=None
    #             root.right=root.left
    #             root.left=None
    #             return tail_2 if tail_2 else tail

    #     formChain(root)
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right=self.prev
        root.left=None
        self.prev=root


            

            