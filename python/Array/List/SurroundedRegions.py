class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d=deque([])
        height=len(board)
        width=len(board[0])
        def dfs(i:int,j:int):
            positions=[]
            d.append((i, j))
            surrounded=True
            while d:
                n=d.popleft()
                positions.append(n)
                if (n[0]==0 or n[0]==height-1 or n[1]==0 or n[1]==width-1):
                    surrounded=False
                for di, dj in (-1, 0), (1, 0), (0, 1), (0, -1):
                    newi=n[0]+di
                    newj=n[1]+dj
                    if (newi >=0 and newi<height and newj>=0 and newj<width and board[newi][newj] == "O"):
                        print(newi, newj)
                        board[newi][newj]="+"
                        d.append((newi, newj))

            if surrounded:
                for i, j in positions:
                    board[i][j]="X"

        for m in range(height):
            for n in range(width):
                if board[m][n] == "O":
                    dfs(m, n)
        
        for m in range(height):
            for n in range(width):
                if board[m][n] == "+":
                    board[m][n] = "O"

    def solveOutwardsIn(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        o = "O"
        
        n = len(board) 
        m = len(board[0])

        Q = deque()
        
        for i in range(n):
            if board[i][0] == o:
                Q.append((i,0))
            if board[i][m-1] == o:
                Q.append((i, m-1))
                
        for j in range(m):
            if board[0][j] == o:
                Q.append((0,j))
            if board[n-1][j] == o:
                Q.append((n-1, j))
                
        def inBounds(i,j):
            return (0 <= i < n) and (0 <= j < m)
                
        while Q:
            i,j = Q.popleft()
            board[i][j] = "#"
            
            for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not inBounds(ii, jj):
                    continue
                if board[ii][jj] != o:
                    continue
                Q.append((ii,jj))
                board[ii][jj] = '#'
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == o:
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = o

    