from collections import deque, List

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        record=dict()

        def traverse(root: Optional[TreeNode], depth:int):
            if not root:
                return
            
            if depth not in record:
                record[depth]=[1, root.val]
            else:
                record[depth][0]+=1
                record[depth][1]+=root.val

            traverse(root.left, depth+1)
            traverse(root.right, depth+1)

        traverse(root, 0)
        res=[]
        for l in record.values():
            res.append(l[1]/l[0])
        return res
        
    def averageOfLevelsUsingDeque(self, root: Optional[TreeNode]) -> List[float]:
        d = deque([root])
        res=[]
        while d:
            row=[]
            for i in range(len(d)):
                n=d.popleft()
                row.append(n.val)
                if n.left:
                    d.append(n.left)
                if n.right:
                    d.append(n.right)
            res.append(sum(row)/len(row))
        return res
