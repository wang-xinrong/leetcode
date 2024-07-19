# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # in every iteration
        root = TreeNode(val=preorder[0])
        if len(preorder)==1: return root

        leftlen=0
        while inorder[leftlen]!=root.val:
            leftlen+=1
        
        leftpreorder=preorder[1:leftlen+1]
        leftinorder=inorder[:leftlen]

        rightpreorder=rightinorder=[]
        if leftlen+1 < len(preorder):
            rightpreorder=preorder[leftlen+1:]
            rightinorder=inorder[leftlen+1:]
        
        if leftpreorder:
            root.left=self.buildTree(leftpreorder, leftinorder)
        if rightpreorder:
            root.right=self.buildTree(rightpreorder, rightinorder)

        return root
    
    def buildTreeFaster(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        rootval=preorder[0]
        index=inorder.index(rootval)
        root=TreeNode(val=rootval)
        root.left=self.buildTree(preorder[1:index+1], inorder[:index])
        root.right=self.buildTree(preorder[index+1:], inorder[index+1:])
        return root