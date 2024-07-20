# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d=deque([root])
        res=[]
        while d:
            temp=[]
            for i in range(len(d)):
                n=d.popleft()
                temp.append(n.val)
                if n.left:
                    d.append(n.left)
                if n.right:
                    d.append(n.right)
            res.append(temp)
        return res