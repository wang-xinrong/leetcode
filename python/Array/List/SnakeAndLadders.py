class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        d=deque([1])
        order=1
        nghr=[]
        visited=set([1])
        steps=0
        for m in range(len(board)-1, -1, -1):
            nghr+=board[m][::order]
            order*=-1
        while d:
            steps+=1
            for i in range(len(d)):
                temp=d.popleft()
                for j in range(1, 7, 1):
                    if temp+j==len(board)**2:
                        return steps
                    if temp+j>len(nghr):
                        continue
                    if temp+j not in visited:
                        visited.add(temp+j)
                        if nghr[temp+j-1]!=-1:
                            if nghr[temp+j-1]==len(board)**2:
                                return steps
                            d.append(nghr[temp+j-1])
                        else:
                            d.append(temp+j)
        
        return -1