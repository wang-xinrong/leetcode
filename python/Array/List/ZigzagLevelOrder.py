class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lefttoright=True
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
            if lefttoright:
                res.append(temp)
            else:
                res.append(temp[::-1])
            lefttoright=not lefttoright

        return res